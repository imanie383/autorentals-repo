# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.vehicle'

    plate = fields.Char(required=True)
    cartype_id = fields.Many2one('autorentas.cartype')
    brand_id = fields.Many2one('autorentas.brand')
    model_id = fields.Many2one('autorentas.model')
    color = fields.Char(required=True)
    description = fields.Text()

    now = datetime.datetime.now()
    now = now.year
    
    year=fields.Char(default = now, required=True)
    price = fields.Float()