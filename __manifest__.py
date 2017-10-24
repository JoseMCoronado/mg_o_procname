# -*- coding: utf-8 -*-
{
    'name': 'Write Sale Order Line Description on Purchase Order Line (Dropship)',
    'category': 'Purchase',
    'author': 'Jose M. Coronado',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
On a button click writes the name of the procurement order (i.e. sale order line name) to the purchase order line.
        """,
    'depends': ['base','stock_account','stock_dropshipping','purchase'],
    'data': [
        'data/ir_model_fields.xml',
        'data/ir_actions_server.xml',
        'data/ir_ui_view.xml',

    ],
    'installable': True,
}
