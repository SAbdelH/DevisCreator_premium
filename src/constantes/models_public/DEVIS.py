a = {
    'name': 'devis',
    'schema': 'activites',
    'columns': {
        'numero_devis': {
            'type': 'String',
            'primary_key': True,
            'autoincrement': False,
            'nullable': False
        },
        'objet': {
            'type': 'String'
        },
        'produit': {
            'type': 'String'
        },
        'prix_unite': {
            'type': 'Numeric',
            'type_params': {
                'precision': 10,
                'scale': 3
            }
        },
        'quantite': {
            'type': 'Integer'
        },
        'remise': {
            'type': 'Numeric',
            'type_params': {
                'precision': 10,
                'scale': 3
            }
        },
        'type_remise': {
            'type': 'String'
        },
        'prix': {
            'type': 'Numeric',
            'type_params': {
                'precision': 10,
                'scale': 3
            }
        },
        'client': {
            'type': 'String'
        },
        'mail_client': {
            'type': 'String'
        },
        'tel_client': {
            'type': 'String'
        },
        'crea_date': {
            'type': 'Date'
        },
        'crea_user': {
            'type': 'String'
        }
    },
    'constraints': None
}