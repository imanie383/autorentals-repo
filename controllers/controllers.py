# -*- coding: utf-8 -*-
from odoo import http

# class Autorentas(http.Controller):
#     @http.route('/autorentas/autorentas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/autorentas/autorentas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('autorentas.listing', {
#             'root': '/autorentas/autorentas',
#             'objects': http.request.env['autorentas.autorentas'].search([]),
#         })

#     @http.route('/autorentas/autorentas/objects/<model("autorentas.autorentas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('autorentas.object', {
#             'object': obj
#         })