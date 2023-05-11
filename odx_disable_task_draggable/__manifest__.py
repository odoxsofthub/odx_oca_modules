# -*- coding:utf-8 -*-
{
    'name': 'Disable Task Stage Drag & Drop',
    'version': '13.0.1.0',
    'summary': """
       The drag and drop of Task stage can be restricted from the kanban view by enabling the access group for
        the particular user
       """,
    'category': 'project',
    'author': 'Odox SoftHub',
    'description': """The drag and drop of Task stage can be restricted from the kanban
     view by enabling the access group for the particular user""",
    'website': 'https://www.odoxsofthub.com',
    'depends': ['base', 'project'],
    'data': [
        'security/security.xml',
        'views/project_view.xml',
    ],
    'images': ['static/description/thumbnail.gif'],
    'installable': True,
    'application': True,
}
