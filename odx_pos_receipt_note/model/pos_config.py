# -*- coding: utf-8 -*-
from odoo import models, fields, api


class POSConfig(models.Model):
    _inherit = 'pos.config'

    iface_orderline_pos_order_notes = fields.Boolean(string='Orderline Notes', help='Allow custom notes on Orderlines.')

    @api.onchange('module_pos_restaurant')
    def _onchange_module_pos_restaurant(self):
        if not self.module_pos_restaurant:
            self.update({'iface_printbill': False,
                         'iface_splitbill': False,
                         'is_order_printer': False,
                         'is_table_management': False,
                         'iface_orderline_notes': False,
                         'iface_orderline_pos_order_notes': True})

        else:
            self.update({'iface_orderline_pos_order_notes': False})
