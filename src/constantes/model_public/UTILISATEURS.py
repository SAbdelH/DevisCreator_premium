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
    },
    # Index unique sur identifiant
    {
        'type': 'Index',
        'name': 'uq_identifiant',
        'columns': ['identifiant'],
        'unique': True
    },
    # Index sur role
    {
        'type': 'Index',
        'name': 'idx_role',
        'columns': ['role']
    },
    # Index sur poste
    {
        'type': 'Index',
        'name': 'idx_poste',
        'columns': ['poste']
    },
    # Index sur group_id
    {
        'type': 'Index',
        'name': 'idx_group_id',
        'columns': ['group_id']
    },
    # Index composé sur nom et prénom
    {
        'type': 'Index',
        'name': 'idx_nom_prenom',
        'columns': ['nom', 'prenom']
    }
]
}