from odoo import fields, models,api

class PosReport(models.Model):
    _inherit = 'pos.order'
    

# class Poscontact(models.Model):
#     _inherit = 'res.partner'
#
# class Poscontacts(models.Model):
#     _inherit = 'res.users'
