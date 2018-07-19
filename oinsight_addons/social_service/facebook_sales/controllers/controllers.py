# -*- coding: utf-8 -*-
from odoo import http

# class FacebookSales(http.Controller):
#     @http.route('/facebook_sales/facebook_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facebook_sales/facebook_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facebook_sales.listing', {
#             'root': '/facebook_sales/facebook_sales',
#             'objects': http.request.env['facebook_sales.facebook_sales'].search([]),
#         })

#     @http.route('/facebook_sales/facebook_sales/objects/<model("facebook_sales.facebook_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facebook_sales.object', {
#             'object': obj
#         })