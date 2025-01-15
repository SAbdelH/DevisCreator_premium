{
    "nom": (
        lambda val, liste_name: "_le_inventory_name" if liste_name == "_lw_inventory_list_inventory" else "_le_invoice_name",
        "setText",
        lambda val, liste_name: val,
    ),
    "marque": (
        lambda val, liste_name: "_le_inventory_marque"if liste_name == "_lw_inventory_list_inventory" else "_le_invoice_marque",
        "setText",
        lambda val, liste_name: val
    ),
    "prix": (
        lambda val, liste_name: "_ds_inventory_price" if liste_name == "_lw_inventory_list_inventory" else "_ds_invoice_price",
        "setValue",
        lambda val, liste_name: float(val) if val else 0,
    ),
    "quantite": (
        lambda val, liste_name: "_s_inventory_quantity",
        "setValue",
        lambda val, liste_name: int(val) if val else 0,
    ),
    "remise": (
        lambda val, liste_name: "_ds_inventory_remise" if liste_name == "_lw_inventory_list_inventory" else "_ds_invoice_remise",
        "setValue",
        lambda val, liste_name: float(val) if val else 0,
    ),
    "type_remise": (
        lambda val, liste_name: "_cbx_inventory_type_remise" if liste_name == "_lw_inventory_list_inventory" else "_cbx_invoice_type_remise",
        "setCurrentIndex",
        lambda val, liste_name: (1 if val == "€" else 2 if val == "%" else 0)
    ),
    "date_fabric": (
        lambda val, liste_name: "_de_inventory_fabric",
        "setDate",
        lambda val, liste_name: (QDate.fromString(val, "dd-MM-yyyy") if val else QDate.currentDate()),
    ),
    'quantifiable' : (
        lambda val, liste_name: "_cb_inventory_quantifiable" if liste_name == "_lw_inventory_list_inventory" else "_cb_invoice_quantifiable",
        "setChecked",
        lambda val, liste_name: val,
    ),
    'louable' : (
        lambda val, liste_name: "_cb_inventory_location" if liste_name == "_lw_inventory_list_inventory" else "_cb_invoice_location",
        "setChecked",
        lambda val, liste_name: val,
    )
}