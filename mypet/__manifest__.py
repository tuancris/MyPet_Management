# -*- coding: utf-8 -*-
{
    'name': "My pet - tuan .info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "tuancris.info",
    'website': "https://tuan.info",
    'category': 'Uncategorized',
    'version': '-100',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
