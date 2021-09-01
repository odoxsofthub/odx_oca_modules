# -*- coding: utf-8 -*-
{
    'name': 'Notes in POS receipt',
    'version': '14.0.2.0',
    'summary': """
      Add notes in POS receipt
       """,
    'category': 'Point of Sale',
    'author': 'Odox SoftHub',
    'description': """Add notes in POS receipt""",
    'website': 'http://www.odoxsofthub.com',
    'depends': ['base', 'point_of_sale', 'pos_restaurant'],
    'data': [
        'views/view.xml',
        'views/pos_order.xml',
        'views/pos_config_views.xml',
    ],
    'qweb': [
        'static/src/xml/ReceiptScreen.xml'
    ],
    'images': ['static/description/thumbnail.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,

}
