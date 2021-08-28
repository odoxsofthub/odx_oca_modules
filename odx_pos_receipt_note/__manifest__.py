# -*- coding: utf-8 -*-
{
    'name': 'Notes in pos receipt',
    'version': '14.0',
    'summary': """
      Add notes in pos receipt
       """,
    'category': 'Point of Sale',
    'author': 'Odox SoftHub',
    'description': """Add notes in pos receipt""",
    'website': 'http://www.odoxsofthub.com',
    'depends': ['base', 'point_of_sale', 'pos_restaurant'],
    'data': [
        'views/view.xml',
        'views/pos_order.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/ReceiptScreen.xml'
    ],
}
