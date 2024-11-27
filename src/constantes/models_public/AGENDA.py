{
    'name': 'agenda',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'titre': {'type': 'String'},
        'description': {'type': 'String'},
        'jour': {'type': 'Date', 'nullable': False},
        'heure_debut': {'type': 'Time', 'nullable': False},
        'heure_fin': {'type': 'Time', 'nullable': False},
        'crea_user': {'type': 'String'}
    },
    'constraints': None
    }