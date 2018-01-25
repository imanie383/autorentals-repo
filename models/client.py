# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autorentas(models.Model):
    _name = 'autorentas.client'

    name = fields.Char(required=True)
    lastname = fields.Char(required=True)

    street = fields.Char(required=True)
    neighourhood = fields.Char(required=True)
    interior = fields.Char()
    outdoor = fields.Integer(required=True)