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
        'type': 'DateTime','type_params': {'timezone': False}, 'default': 'func.now()', 'onupdate': 'func.now()'
    },
},
'constraints': [
    # Index sur id
    {
        'type': 'Index',
        'name': 'idx_client_id',
        'columns': ['id'],
        'unique': True
    },
    # Index sur id
    {
        'type': 'Index',
        'name': 'idx_client_nom',
        'columns': ['nom']
    }
]
}