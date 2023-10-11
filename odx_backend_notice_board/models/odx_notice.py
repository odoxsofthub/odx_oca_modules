# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from datetime import date
from odoo.exceptions import AccessError


class NoticeBoard(models.Model):
    _name = 'odx.notice.board'
    _description = 'For posting announcements, news, events, and other information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'

    name = fields.Char(
        string="Name",
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    notice_title = fields.Char(string='Title', tracking=True)
    notice_category = fields.Many2one('odx.notice.type', string='Category', tracking=True)
    notice_type = fields.Char(related='notice_category.name')
    notice_description = fields.Html(string='Notice Content')
    attachments = fields.Many2many('ir.attachment', string='Attachments')
    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    ], default='draft', string='Status', tracking=True)
    announcement = fields.Html(string='Note')
    notify_group_id = fields.Many2one('res.groups', string='Group')
    published_date = fields.Date(string="Notice Published Date")
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority',
                                index=True, tracking=True)
    email_status = fields.Boolean(string='Email Status', defualt=False, tracking=True)
    badge_focus = fields.Boolean(default=False, string='Focus', compute="_compute_badge_focus")
    badge_text = fields.Char(String='Badge Text', default="New", )
    start_date = fields.Date(string='Start Date', default=lambda self: date.today())
    end_date = fields.Date(string="End Date")
    badge_color = fields.Selection([
        ('green', 'Green'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('black', 'Black')
    ], default='red', string='Badge Color')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('odx.notice.board') or "New"
        return super(NoticeBoard, self).create(vals)



    def action_done(self):
        self.state = 'published'
        self.published_date = datetime.now().date()

    def action_draft(self):
        self.state = 'draft'
        self.published_date = False

    def action_cancel(self):
        self.state = 'unpublished'

    def notice_view_form(self):
        view_id = self.env.ref('odx_backend_notice_board.odx_notice_board_view_form_wizard').id
        return {'type': 'ir.actions.act_window',
                'name': self.name,
                'res_model': 'odx.notice.board',
                'target': 'new',
                'view_mode': 'form',
                'res_id': self.id,
                'view_id': view_id,
                'views': [[view_id, 'form']],
                }

    def _compute_badge_focus(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.badge_focus = True
            elif rec.start_date:
                rec.badge_focus = True
            elif rec.end_date:
                rec.badge_focus = True
            else:
                rec.badge_focus = False

    def send_by_mail(self):
        if self.email_status == False:
            view = self.env.ref('odx_backend_notice_board.send_notice_wiz_form_view')
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            db_name = self.env.cr.dbname
            base_url += '/web?db=' + db_name + '#id=%d&view_type=form&model=%s' % (self.id, self._name)
            redirect_url = ''
            redirect_url = base_url
            name = self.name
            return {
                'name': "Send Mail",
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'send.notice.wiz',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'context': {'default_name': self.name,
                            'default_notice_content': '<p>Greetings,</p><br/><p>A New Article has been Published ' + name + ' Click to view</p><br/><a href="' + redirect_url + '" style="display: inline-block; padding: 10px 20px; background-color: #007BFF; color: #fff; text-decoration: none; border-radius: 4px;">View</a></p>',
                            'default_user_ids': self.notify_group_id.mapped('users').ids,
                            'default_email_status': self.email_status
                            },
                'target': 'new',
            }
        else:
            raise AccessError(
                _("The email has already been sent. If you wish to resend the email, please set its status to inactive."))
