{
    "nom": (
        lambda val, liste_name: "invNameLine" if liste_name == "invList" else "nameArticleLine",
        "setText",
        lambda val, liste_name: val,
    ),
    "marque": (lambda val, liste_name: "invMarkLine", "setText", lambda val, liste_name: val),
    "prix": (
        lambda val, liste_name: "invPricespinBox" if liste_name == "invList" else "price",
        "setValue",
        lambda val, liste_name: float(val) if val else 0,
    ),
    "quantite": (
        lambda val, liste_name: "invquantityspinBox" if liste_name == "invList" else "dbquantity",
        "setValue",
        lambda val, liste_name: int(val) if val else 0,
    ),
    "remise": (
        lambda val, liste_name: "invpromotionspinBox" if liste_name == "invList" else "remise",
        "setValue",
        lambda val, liste_name: float(val) if val else 0,
    ),
    "type_remise": (
        lambda val, liste_name: "invtypPromocombo" if liste_name == "invList" else "remisecheck",
        lambda val, liste_name: "setCurrentIndex" if liste_name == "invList" else "setChecked",
        (
            lambda val, liste_name: (
                (1 if val == "%" else 0) if liste_name == "invList" else (True if val == "%" else False)
            )
        ),
    ),
    "fabrication_date": (
        lambda val, liste_name: "invfabricDate",
        "setDate",
        lambda val, liste_name: (QDate.fromString(str(val), "yyyy-MM-dd") if val else QDate.currentDate()),
    ),
}