# -*- coding: utf-8 -*-

from odoo import models, fields


class DepartmentType(models.Model):
    _name = 'odx.notice.type'
    _description = ''

    name = fields.Char(string='Notice Category')
