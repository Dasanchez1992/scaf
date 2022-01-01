# -*- coding: utf-8 -*-
{
    'name': "Modulo base del sistema de control de activos fijos (SCAF)",

    'summary': """
        Agregar campos base para el funcionamiento del sistema de control de activos fijos (SCAF)""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Danilo Sanchez",
    'website': "https://www.linkedin.com/in/danilo-sanchez-34a391126/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_setup', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/settings.xml',
        'views/stock_picking.xml',
        'reports/report.xml'
    ],
}
