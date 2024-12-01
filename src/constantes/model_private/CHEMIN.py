{
    'name': 'path',
    'schema': 'informations',
    'columns': {
        'id': {'type': 'Integer', 'primary_key': True, 'autoincrement': True, 'nullable': False},
        'company': {'type': 'String', 'nullable': False},
        'name': {'type': 'String', 'nullable': False},
        'path': {'type': 'String', 'nullable': False}
    },
    'constraints': [
    # Index unique sur id
    {
        'type': 'Index',
        'name': 'uq_path_id',
        'columns': ['id'],
        'unique': True
    }
    ]
    }