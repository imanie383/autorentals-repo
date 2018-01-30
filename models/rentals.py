# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime, date, time


class autorentas(models.Model):
    _name = 'autorentas.rental'

    vehicle_id = fields.Many2one('autorentas.vehicle')
    client_id = fields.Many2one('res.partner')

    date_start = fields.Date()
    date_end = fields.Date()

    total_price = fields.Char()

    @api.onchange('date_start', 'date_end', 'vehicle_id')
    def calculate_price(self):
        if self.date_end and self.date_start: 
            # Read dates
            d0 = datetime.strptime(self.date_start,'%Y-%m-%d')
            d1 = datetime.strptime(self.date_end,'%Y-%m-%d')
            
            # Get the days number
            n_days = d1 - d0
            n_days = str(n_days)
            n_days = n_days.split(' ')
            n_days = n_days[0]
            n_days = float(n_days)
            
            # Get price by day
            a_day = self.vehicle_id.price
            a_day  = float(a_day)

            #Get and write the total
            self.total_price = str(a_day*n_days)