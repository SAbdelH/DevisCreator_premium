{
    'name': 'ui_update',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'nom': {'type': 'String'},
        'crea_date': {'type': 'DateTime', 'type_params': {'timezone': False}, 'default': 'func.now()', 'onupdate': 'func.now()'},
        'crea_user': {'type': 'String'},
    },
    'constraints': [
    # Index sur id
    {
        'type': 'Index',
        'name': 'uq_update_id',
        'columns': ['id'],
        'unique': True
    },
    {
        'type': 'CheckConstraint',
        'condition': "nom IN ('client', 'company', 'dashbord', 'database', 'facture', 'devis', 'inventory', 'restoration', 'user', 'validfacture','agenda')",
        'name': 'check_update_uiname'
    },
    {
        'type': 'Index',
        'name': 'idx_ui_update',
        'columns': ['nom', 'crea_date']
    }
    ]
    }