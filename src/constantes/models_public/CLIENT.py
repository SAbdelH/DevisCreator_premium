{
'name': 'clients',
'schema': 'informations',
'columns': {
    'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
    'nom': {'type': 'String'},
    'telephone': {
        'type': 'String',
        'type_params': {'length': 120},
        'nullable': True
    },
    'email': {
            'type': 'String',
            'type_params': {'length': 120},
            'nullable': True
        },
    'commerce': {
            'type': 'Numeric',
            'type_params': {
                'precision': 10,
                'scale': 3
            }
        },
    'crea_date': {
        'type': 'Date'
    },
}
}