{
    'name': 'activites',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'crea_date': {'type': 'DateTime', 'type_params': {'timezone': False}, 'default': 'func.now()', 'onupdate': 'func.now()'},
        'activites': {'type': 'String'},
        'action': {'type': 'String'},
        'budget': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}}
    },
    'constraints': [
    # Index composé
    {
        'type': 'Index',
        'name': 'idx_activite',
        'columns': ['id', 'crea_date','activites', 'action', 'budget']
    }
    ]
    }