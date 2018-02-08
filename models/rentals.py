# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime, date, time


class autorentas(models.Model):
    _name = 'autorentas.rental'
    _rec_name = 'client_id'

    vehicle_id = fields.Many2one('autorentas.vehicle', required=True)
    client_id = fields.Many2one('res.partner', copy=False, required=True)

    date_start = fields.Date(required=True)
    date_end = fields.Date(required=True)

    total_price = fields.Char(compute="calculate_price")

    _sql_constraints = [
        ('vehicle_unique','UNIQUE(vehicle_id)',
            'This vehicle is already being used'),
        ('client_unique','UNIQUE(client_id)',
            'This client has already rented a car')
    ]

    @api.onchange('date_start', 'date_end', 'vehicle_id')
    def calculate_price(self):
        for record in self:
            if record.date_end and record.date_start: 
                # Read dates
                d0 = datetime.strptime(record.date_start,'%Y-%m-%d')
                d1 = datetime.strptime(record.date_end,'%Y-%m-%d')
                
                if d0 == d1:
                    n_days = 1;

                    # Get price by day
                    a_day = record.vehicle_id.price
                    a_day  = float(a_day)

                    #Get and write the total
                    record.total_price = str(a_day*n_days)
                else:
                    if d0 <= d1:
                        #Get number of days
                        n_days = d1 - d0
                        n_days = str(n_days)
                        n_days = n_days.split(' ')
                        n_days = n_days[0]
                        n_days = float(n_days)

                        print(n_days)
                    
                        # Get price by day
                        a_day = record.vehicle_id.price
                        a_day  = float(a_day)

                        #Get and write the total
                        if n_days>20:
                            a_day = a_day*0.70
                        
                        print(a_day)
                        record.total_price = str(a_day*n_days)
                    else:
                        record.date_start = record.date_end
                        return {
                            'warning' : {
                                'title' : "Error",
                                'message' : "The start date must be before the end date"
                            }
                        }