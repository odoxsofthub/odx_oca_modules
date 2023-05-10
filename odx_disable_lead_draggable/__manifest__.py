# -*- coding:utf-8 -*-
{
    'name': 'Disable Lead Stage Drag & Drop',
    'version': '13.0.1.0',
    'summary': """
       The drag and drop of lead stages can be restricted from the kanban view by enabling the access group for
        the particular user
       """,
    'category': 'crm',
    'author': 'Odox SoftHub',
    'description': """The drag and drop of lead stages can be restricted from the kanban
     view by enabling the access group for the particular user""",
    'website': 'https://www.odoxsofthub.com',
    'depends': ['base', 'crm'],
    'data': [
        'security/security.xml',
        'views/crm_view.xml',
    ],
    'images': ['static/description/thumbnail.gif'],
    'installable': True,
    'application': True,
}
