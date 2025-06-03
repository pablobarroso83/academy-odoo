# -*- coding: utf-8 -*-
{
   'name': 'Gestión Académica',
   
    'summary': 'Gestión de cursos y sesiones académicas',
    
    'description': 'Módulo para administrar cursos, sesiones y participantes.',
    
    'author': "Pablo",
    
    'website': "https://github.com/pablobarroso83",
    
    'application': True,
    
    'installable': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

