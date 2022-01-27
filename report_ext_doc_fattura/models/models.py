# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class report_ext_doc_fattura(models.Model):
#     _name = 'report_ext_doc_fattura.report_ext_doc_fattura'
#     _description = 'report_ext_doc_fattura.report_ext_doc_fattura'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
