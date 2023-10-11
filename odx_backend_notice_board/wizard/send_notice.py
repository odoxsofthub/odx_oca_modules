from odoo import api, fields, models


class SendNoticeWizard(models.TransientModel):
    _name = 'send.notice.wiz'
    _description = 'Send Notice'

    name = fields.Char(string="name")
    subject = fields.Char('Subject', default="Latest Article is Here!")
    notice_content = fields.Html('Content')
    user_ids = fields.Many2many('res.users', string='Recipient')
    email_status = fields.Boolean(string='Email Status')

    def action_send_by_mail(self):
        active_id = self.env['odx.notice.board'].browse(self._context['active_id'])
        # if self.email_status == False:
        partner_ids = False
        if self.user_ids:
            partner_ids = self.user_ids.mapped('partner_id')
        if partner_ids:
            vals = {
                'subject': self.subject,
                'body_html': self.notice_content,
                'partner_ids': partner_ids,
                'model': 'odx.notice.board',
                'recipient_ids': partner_ids,
                'auto_delete': True,
                'email_from': self.env.user.partner_id.email if self.env.user else False,
            }

            mail_sent = self.env['mail.mail'].sudo().create(vals)
            mail_sent.send()
        active_id.email_status = True

