{
    'name': 'entreprise',
    'schema': 'informations',
    'columns': {
        'nom': {
            'type': 'String',
            'primary_key': True,
            'autoincrement': False,
            'nullable': False
        },
        'resp_nom': {
            'type': 'String'
        },
        'resp_prenom': {
            'type': 'String'
        },
        'adresse': {
            'type': 'String'
        },
        'ville': {
            'type': 'String'
        },
        'commune': {
            'type': 'String'
        },
        'code_postal': {
            'type': 'Integer'
        },
        'departement': {
            'type': 'String'
        },
        'mail': {
            'type': 'String'
        },
        'portable': {
            'type': 'String'
        },
        'telephone': {
            'type': 'String'
        },
        'siren': {
            'type': 'String'
        },
        'siret': {
            'type': 'String'
        },
        'code_ape': {
            'type': 'String'
        },
        'iban': {
            'type': 'String'
        },
        'bic': {
            'type': 'String'
        },
        'capital': {
            'type': 'Integer'
        }
    },
    'constraints': [
    # Index composé
    {
        'type': 'Index',
        'name': 'idx_entreprise',
        'columns': ['nom', 'resp_nom', 'resp_prenom', 'adresse','ville', 'commune', 'code_postal', 'departement',
                    'mail', 'portable', 'telephone', 'siren', 'siret', 'code_ape', 'iban', 'bic', 'capital']
    }
    ]
}