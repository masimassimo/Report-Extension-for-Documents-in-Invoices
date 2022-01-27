# -*- coding: utf-8 -*-
{
    'name': "Report Documenti in Fattura",

    'summary': """
        Modulo per aggiungere i Documenti collegati nel PDf delle Fatture""",

    'description': """
        Modulo per aggiungere i Documenti collegati nel PDf delle Fatture
    """,

    'author': "Massimo Masi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_it_fatturapa'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/report.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
