{
'name': 'utilisateurs',
'schema': 'informations',
'columns': {
    'identifiant': {
        'type': 'String',
        'primary_key': True,
        'autoincrement': False,
        'nullable': False,
        'unique': True
    },
    'email': {
        'type': 'String',
        'type_params': {'length': 120},
        'nullable': True
    },
    'password_hash': {
        'type': 'String',
        'type_params': {'length': 128},
        'nullable': False
    },
    'nom': {
        'type': 'String'
    },
    'prenom': {
        'type': 'String'
    },
    'poste': {
        'type': 'String'
    },
    'sexe': {
        'type': 'String',
        'nullable': True
    },
    'role': {
        'type': 'String',
        'nullable': True
    },
    'group_id': {
        'type': 'String',
        'nullable': False
    },
    'expire': {
        'type': 'Date',
        'nullable': True
    },
},
'constraints': [
    {
        'type': 'CheckConstraint',
        'condition': "sexe IN ('Homme', 'Femme')",
        'name': 'check_sexe'
    },
    {
        'type': 'CheckConstraint',
        'condition': "role IN ('Administrateur', 'Responsable', 'Employe')",
        'name': 'check_role'
    }
]
}