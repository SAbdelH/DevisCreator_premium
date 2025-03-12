{
    'name': 'inventaires_evol',
    'schema': 'inventaires',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'reference': {'type': 'String', 'unique': True},
        'nom': {'type': 'String', 'unique': True},
        'ventes': {'type': 'Integer'}
    },
    'constraints': [
    # Index unique sur nom
    {
        'type': 'Index',
        'name': 'uq_inv_evol_nom',
        'columns': ['nom'],
        'unique': True
    },
    ]
}