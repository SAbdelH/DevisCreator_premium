{
    'name': 'achat',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'nom': {'type': 'String'},
        'reference': {'type': 'String'},
        'prix': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}},
        'quantite': {'type': 'Integer'},
        'crea_date': {'type': 'DateTime', 'type_params': {'timezone': False}, 'default': 'func.now()', 'onupdate': 'func.now()'},
        'crea_user': {'type': 'String'},
    },
    'constraints': [
    # Index sur id
    {
        'type': 'Index',
        'name': 'uq_achat_id',
        'columns': ['id'],
        'unique': True
    }
    ]
    }