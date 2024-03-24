# -*- coding: utf-8 -*-
{
    'name': "Serah-In Update reports",
    'summary': """Serah-In personnalize les rapport de base d'odoo telque le rapport du bon de commande, 
            livraison et facture""",
    'description': """Serah-In personnalize les rapport de base d'odoo telque le rapport du bon de commande, 
            livraison et facture""",
    'author': "SIMO LARISSA",
    'website': "https://github.com/Net-2s/serah_update_reports",
    'category': 'Uncategorized',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       'reports/sale_report_template_inherit.xml',
       'reports/delivery_report_template_inherit.xml',
       'reports/invoice_report_template_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
