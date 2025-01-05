{
'name': 'factures',
'schema': 'activites',
'columns': {
    'numero_facture': {
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
    },
    "paye": {
        "type" : "Boolean"
    }
},
'constraints': [
    # Index unique sur identifiant
    {
        'type': 'Index',
        'name': 'uq_numero_facture_facture',
        'columns': ['numero_facture'],
        'unique': True
    },
    # Index sur quantité
    {
        'type': 'Index',
        'name': 'idx_facture_quantite',
        'columns': ['quantite']
    },
    # Index sur prix
    {
        'type': 'Index',
        'name': 'idx_facture_prix',
        'columns': ['prix']
    },
    # Index sur client
    {
        'type': 'Index',
        'name': 'idx_facture_client',
        'columns': ['client']
    },
]
}