# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.vehicle'
    _rec_name='plate'
    
    plate = fields.Char(required=True)
    brand_id = fields.Many2one('autorentas.brand')
    model_id = fields.Many2one('autorentas.model')
    color = fields.Char(required=True)
    description = fields.Text()

    #Actual year
    now = datetime.datetime.now()
    now = now.year
    
    year=fields.Char(default = now, required=True)
    price = fields.Float()


    sql_constraints = [
        ('plate_unique', 'UNIQUE(plate)', "The plate must be unique" )
    ]