# -*- coding: utf-8 -*-
{
    'name': "My pet (+) - tuan.info",
    'summary': """My pet plus""",
    'description': """Managing pet information""",
    'author': "tuancris.info",
    'website': "https://tuan.info",
    'category': 'Uncategorized',
    'version': '-100',
    'depends': [
        'mypet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_plus_views.xml',
        'views/product_pet_views.xml',
        'views/my_pet_views.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
