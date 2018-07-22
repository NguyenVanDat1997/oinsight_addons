# -*- coding: utf-8 -*-
from odoo import http

# class Facebook(http.Controller):
#     @http.route('/facebook/facebook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facebook/facebook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('facebook.listing', {
#             'root': '/facebook/facebook',
#             'objects': http.request.env['facebook.facebook'].search([]),
#         })

#     @http.route('/facebook/facebook/objects/<model("facebook.facebook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facebook.object', {
#             'object': obj
#         })