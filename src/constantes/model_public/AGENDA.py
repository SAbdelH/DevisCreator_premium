{
    'name': 'agenda',
    'schema': 'activites',
    'columns': {
        'id': {'type': 'BigInteger', 'primary_key': True, 'autoincrement': True},
        'titre': {'type': 'String'},
        'description': {'type': 'String', 'type_params': {'length': 60}},
        'jour': {'type': 'Date', 'nullable': False},
        'heure_debut': {'type': 'Time', 'nullable': False},
        'heure_fin': {'type': 'Time', 'nullable': False},
        'crea_user': {'type': 'String'}
    },
    'constraints': [
    # Index sur user
    {
        'type': 'Index',
        'name': 'idx_agenda_user',
        'columns': ['crea_user']
    },
    # Index composé sur nom et prénom
    {
        'type': 'Index',
        'name': 'idx_agenda',
        'columns': ['titre', 'jour', 'heure_debut', 'heure_fin']
    }
    ]
    }