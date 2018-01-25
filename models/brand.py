# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.brand'

    name = fields.Char(required=True)
    country = fields.Char(required=True)