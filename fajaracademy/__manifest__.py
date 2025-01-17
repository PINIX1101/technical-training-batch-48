# -*- coding: utf-8 -*-
{
    'name': "Fajar Academy",

    'summary': "Academy Module",

    'description': """
An Education Module
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'data/fajaracademy_course_data.xml',

        'wizards/add_session_attendees_wizard_view.xml',

        'views/menu_views.xml',
        'views/fajaracademy_course.xml',
        'views/fajaracademy_session.xml',
        'views/res_partner.xml',
        'views/partner_categories.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

