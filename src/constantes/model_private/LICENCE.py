{
    'name': 'licences',
    'schema': 'public',
    'columns': {
        'id': {'type': 'Integer', 'primary_key': True, 'autoincrement': True, 'nullable': False},
        'licence_key': {'type': 'String', 'nullable': False},
        'group_id': {'type': 'String', 'nullable': False},
        'abonnement': {'type': 'String', 'nullable': False, 'default': 'basic'},
        'is_active': {'type': 'Boolean', 'default': True},
        'crea_date': {'type': 'DateTime', 'type_params': {'timezone': True}, 'nullable': False}
    },
    'constraints': [
        {
        'type': 'CheckConstraint',
        'condition': "abonnement IN ('basic', 'premium')",
        'name': 'check_abonnement'
    },
    # Index sur group_id
    {
        'type': 'Index',
        'name': 'idx_group_id',
        'columns': ['group_id']
    }
    ]
    }