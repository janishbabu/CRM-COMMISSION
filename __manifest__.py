{
    'name': "CRM commission",
    'version': "16.0.1",
    'sequence': -10,
    'category': 'CRM',
    'author': 'JANISH BABU EK',
    'installable': True,
    'application': True,

    'depends': ['base', 'crm', 'sale', ],
    'data': ['security/ir.model.access.csv',
             'views/sale_order.xml',
             'views/sales_team.xml',
             'views/crm_commission.xml',
             'views/crm_commission_menu.xml',
             ]
}
