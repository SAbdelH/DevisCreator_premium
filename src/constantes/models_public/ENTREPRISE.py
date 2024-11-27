{
    'name': 'entreprise',
    'schema': 'informations',
    'columns': {
        'nom': {
            'type': 'String',
            'primary_key': True,
            'autoincrement': False,
            'nullable': False
        },
        'patron': {
            'type': 'String'
        },
        'adresse': {
            'type': 'String'
        },
        'ville': {
            'type': 'String'
        },
        'commune': {
            'type': 'String'
        },
        'code_postal': {
            'type': 'Integer'
        },
        'departement': {
            'type': 'String'
        },
        'mail': {
            'type': 'String'
        },
        'telephone': {
            'type': 'String'
        },
        'siren': {
            'type': 'String'
        },
        'siret': {
            'type': 'String'
        },
        'code_ape': {
            'type': 'String'
        },
        'iban': {
            'type': 'String'
        },
        'bic': {
            'type': 'String'
        },
        'capital': {
            'type': 'Integer'
        }
    },
    'constraints': None
}