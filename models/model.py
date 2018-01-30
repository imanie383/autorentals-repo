# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.model'

    name = fields.Char(required=True)
    cartype_id = fields.Many2one('autorentas.cartype', required=True)
    brand_id = fields.Many2one('autorentas.brand', required=True)
    description = fields.Text()