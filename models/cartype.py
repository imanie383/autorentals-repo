# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.cartype'

    name = fields.Char(required=True)
    description = fields.Text()