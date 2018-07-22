# -*- coding: utf-8 -*-
from odoo import http

# class CustomWebClient(http.Controller):
#     @http.route('/custom_web_client/custom_web_client/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_web_client/custom_web_client/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_web_client.listing', {
#             'root': '/custom_web_client/custom_web_client',
#             'objects': http.request.env['custom_web_client.custom_web_client'].search([]),
#         })

#     @http.route('/custom_web_client/custom_web_client/objects/<model("custom_web_client.custom_web_client"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_web_client.object', {
#             'object': obj
#         })