# -*- coding: utf-8 -*-
{
    'name': "scaf_sequence_products_by_serial",

    'summary': """
        Genera la secuencia de los productos individualmente por el numero de lotes y el default code del producto
        padre""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Danilo Sanchez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_category.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'data/demo.xml',
    # ],
}
