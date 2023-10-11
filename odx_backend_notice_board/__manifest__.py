# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Backend Notice Board',
    'version': '13.0',
    'author': 'Odox SoftHub',
    'summary': 'A platform for communication and sharing important information.',
    'sequence': 1,
    'description': """ The Backend Notice Board module simplifies internal communication, allowing you to 
    share announcements and messages broadly or to specific groups within your organization, enhancing 
    communication flexibility.
     """,
    'category': 'Services/Tool',
    'website': 'https://www.odoxsofthub.com',
    'support': 'support@odoxsofthub.com',
    'images': [],
    'depends': [
        'mail',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Data
        'data/data.xml',
        # views
        'security/security.xml',
        'views/odx_notice.xml',
        'views/configuration.xml',
        "views/asset_views.xml",
        'views/odx_notice_board_view.xml',
        'views/menus.xml',
        'wizard/send_notice.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'icon': '/odx_backend_notice_board/static/description/icon (1).png',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/noticeboard.gif'],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False
}
