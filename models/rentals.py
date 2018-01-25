#!/usr/bin/python
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import timedelta


class autorentas(models.Model):

    _name = 'autorentas.rental'

    vehicle_id = fields.Many2one('autorentas.vehicle')
    client_id = fields.Many2one('autorentas.client')

    date_start = fields.Date()
    date_end = fields.Date()

    total_price = fields.Float()

    @api.onchange('date_start', 'date_end', 'vehicle_id')
    def calculate_price(self):

        # return vehiculo.precio * (dia_fin-dia_inicio

        a_day = self.vehicle_id.price
        delta = self.date_end - self.date_start
        print(delta)