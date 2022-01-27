# -*- coding: utf-8 -*-
# from odoo import http


# class ReportExtDocFattura(http.Controller):
#     @http.route('/report_ext_doc_fattura/report_ext_doc_fattura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_ext_doc_fattura/report_ext_doc_fattura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_ext_doc_fattura.listing', {
#             'root': '/report_ext_doc_fattura/report_ext_doc_fattura',
#             'objects': http.request.env['report_ext_doc_fattura.report_ext_doc_fattura'].search([]),
#         })

#     @http.route('/report_ext_doc_fattura/report_ext_doc_fattura/objects/<model("report_ext_doc_fattura.report_ext_doc_fattura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_ext_doc_fattura.object', {
#             'object': obj
#         })
