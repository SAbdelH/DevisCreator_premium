{
    'name': 'group',
    'schema': 'public',
    'columns': {
        'id': {'type': 'Integer', 'primary_key': True, 'autoincrement': False, 'nullable': False},
        'nom': {'type': 'String'}
    },
    'constraints': [
    # Index sur id
    {
        'type': 'Index',
        'name': 'uq_group_id',
        'columns': ['id'],
        'unique': True
    }
    ]
    }