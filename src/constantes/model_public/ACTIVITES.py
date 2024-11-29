{
    'name': 'activites',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'crea_date': {'type': 'Date'},
        'activites': {'type': 'String'},
        'action': {'type': 'String'},
        'budget': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}}
    },
    'constraints': None
    }