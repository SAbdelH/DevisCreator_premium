{
    'name': 'inventaires',
    'schema': 'inventaires',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'nom': {'type': 'String', 'unique': True},
        'reference': {'type': 'String', 'unique': True},
        'prix': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}},
        'tva': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}},
        'marque': {'type': 'String'},
        'quantite': {'type': 'Integer'},
        'remise': {'type': 'Numeric', 'type_params': {'precision': 10, 'scale': 3}},
        'type_remise': {'type': 'String'},
        'quantifiable' : {'type': 'Boolean', 'default': True},
        'louable' : {'type': 'Boolean', 'default': False},
        'date_fabric': {'type': 'Date'},
        'crea_user': {'type': 'String'},
    },
    'constraints': [
    # Index unique sur nom
    {
        'type': 'Index',
        'name': 'uq_inv_nom',
        'columns': ['nom'],
        'unique': True
    },
    ]
}