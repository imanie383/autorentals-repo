# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.model'

    name = fields.Char(required=True)
    cartype_id = fields.Many2one('autorentas.cartype')
    brand_id = fields.Many2one('autorentas.brand')
    description = fields.Text()