{
'name': 'devis',
'schema': 'activites',
'columns': {
    'numero_devis': {
        'type': 'String',
        'primary_key': True,
        'autoincrement': False,
        'nullable': False
    },
    'objet': {
        'type': 'String'
    },
    'produit': {
        'type': 'String'
    },
    'prix_unite': {
        'type': 'Numeric',
        'type_params': {
            'precision': 10,
            'scale': 3
        }
    },
    'quantite': {
        'type': 'Integer'
    },
    'remise': {
        'type': 'Numeric',
        'type_params': {
            'precision': 10,
            'scale': 3
        }
    },
    'type_remise': {
        'type': 'String'
    },
    'prix': {
        'type': 'Numeric',
        'type_params': {
            'precision': 10,
            'scale': 3
        }
    },
    'client': {
        'type': 'String'
    },
    'mail_client': {
        'type': 'String'
    },
    'tel_client': {
        'type': 'String'
    },
    'crea_date': {
        'type': 'DateTime', 'type_params': {'timezone': False}, 'default': 'func.now()', 'onupdate': 'func.now()'
    },
    'crea_user': {
        'type': 'String'
    },
    'total_remise': {
        'type': 'Numeric',
        'type_params': {
            'precision': 10,
            'scale': 3
        }
    }
},
'constraints': [
    # Index unique sur identifiant
    {
        'type': 'Index',
        'name': 'uq_numero_devis_devis',
        'columns': ['numero_devis'],
        'unique': True
    },
    # Index sur quantité
    {
        'type': 'Index',
        'name': 'idx_devis_quantite',
        'columns': ['quantite']
    },
    # Index sur prix
    {
        'type': 'Index',
        'name': 'idx_devis_prix',
        'columns': ['prix']
    },
    # Index sur client
    {
        'type': 'Index',
        'name': 'idx_devis_client',
        'columns': ['client']
    },
]
}