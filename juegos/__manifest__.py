# -*- coding: utf-8 -*-
{
    'name': "Juegos",

    'summary': """
        Modulo para hacer seguimiento de videojuegos""",

    'description': """
        Realiza seguimiento de videojuegos categorizandolos por desarrolladora, plataforma (dentro de esta, la consola) y nombre .
    """,

    'author': "Izedra",
    #'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Seguimiento',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/juegos.xml',
        'views/plataformas.xml',
	'views/consolas.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
