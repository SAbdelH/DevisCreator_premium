from datetime import datetime
from functools import partial
from pathlib import Path

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QApplication
from sqlalchemy import text, func

from forms.gui import InventoryItem
from processing.database.model_private import Chemin
from processing.database.model_public import Ui_Update, Inventaires
from processing.database.session import WorkSession


def populateListInventory(self, liste: QListWidget, filter_text: str = "", page: str | None = None):
    _LIST_NAME = liste.objectName()

    with self.Session() as session:
        update = Ui_Update(
        ).verify_update(session,
                        'inventory',
                        filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant
                        )
        first = self.maindialog.firstOpenInventory if page == "_p_inventory" else \
            self.maindialog.firstOpenFacture if page == "factures" else self.maindialog.firstOpenDevis
        if first and page == "_p_inventory":
            self.maindialog.mp_last_update = datetime.now()
        else:
            self.maindialog.ip_last_update = datetime.now()

        updt = ((update and update.crea_date > self.maindialog.mp_last_update) if page == "_p_inventory"
                else (update and update.crea_date > self.maindialog.ip_last_update))

        if first or updt or filter_text:
            session.execute(text("SET lc_time TO 'fr_FR.UTF-8';"))
            query = session.query(
                Inventaires.nom,
                Inventaires.prix,
                Inventaires.marque,
                Inventaires.quantite,
                Inventaires.remise,
                Inventaires.type_remise,
                Inventaires.quantifiable,
                Inventaires.louable,
                func.to_char(Inventaires.date_fabric, 'DD-MM-YYYY').label('date_fabric')
            ).order_by(Inventaires.nom)

            self.maindialog._l_inventory_sum_value.setText(str(query.count()))
            # Ajouter un filtre basé sur le texte saisi
            if filter_text:
                query = query.filter(Inventaires.nom.ilike(f"%{filter_text}%"))
            inventaires = query.all()

            if inventaires:
                ContentPath = {}
                with self.privateSession() as privateSession:
                    inventory_path = privateSession.query(Chemin.path).filter(Chemin.name == 'inventaire').first()
                    if inventory_path:
                        ContentPath = {
                            file.stem: file.as_posix() for file in Path(inventory_path[0]).rglob("*")
                        }
                        if _LIST_NAME == "_lw_inventory_list_inventory":
                            self.maindialog._lw_inventory_list_inventory.setStyleSheet(f"""
                            #_lw_inventory_list_inventory {{
                                background-color: transparent;
                                background: transparent;
                                background-image: url('');
                                background-repeat: no-repeat;
                                background-position: center center;
                                background-origin: content;
                            }}
                            """)
                all_Inventory_list_populate(self, inventaires, ContentPath, _LIST_NAME, filter_text != "")

            if page == "_p_inventory":
                self.maindialog.firstOpenInventory = False
            elif page == "factures":
                self.maindialog.firstOpenFacture = False
            else:
                self.maindialog.firstOpenDevis = False

    if _LIST_NAME == "_lw_inventory_list_inventory" and liste.count() < 1:
        self.maindialog._lw_inventory_list_inventory.setStyleSheet(f"""
                                                                    #_lw_inventory_list_inventory {{
                                                                        background-color: transparent;
                                                                        background: transparent;
                                                                        background-image: url({self.maindialog.inventory_bg});
                                                                        background-repeat: no-repeat;
                                                                        background-position: center center;
                                                                        background-origin: content;
                                                                    }}
                                                                    """)

def all_Inventory_list_populate(self, inventaires, ContentPath, _LIST_NAME, filter: bool = False):
    dlg = self.maindialog
    __allList = [dlg._lw_inventory_list_inventory, dlg._lw_invoice_list_inventory]
    listes = [LW for LW in __allList if LW.objectName() == _LIST_NAME] if filter else __allList
    for liste in listes:
        liste.clear()
        for inventaire in inventaires:
            info = Inventaires.to_dict(inventaire)
            info["icon"] = ContentPath.get(inventaire.nom)
            if liste.objectName() == "_lw_inventory_list_inventory":
                item = QListWidgetItem(liste)
                custom_widget = InventoryItem(info)
                custom_widget.setTheme(dlg.apparence)
                item.setSizeHint(custom_widget.sizeHint())
            else:
                icon = QIcon(ContentPath.get(inventaire.nom))
                item = QListWidgetItem(icon, inventaire.nom)

            item.setData(Qt.UserRole, info)
            # Ajuste la taille de l'item selon le widget
            liste.addItem(item)
            if liste.objectName() == "_lw_inventory_list_inventory":
                liste.setItemWidget(item, custom_widget)

        dlg.mp_last_update = datetime.now().date()

        liste.itemClicked.connect(lambda item: onInventoryItemSelected(self, item,_LIST_NAME))

def onInventoryItemSelected(self, item: QListWidgetItem, liste_name: str):
    dlg = self.maindialog
    inventory_row = item.data(Qt.UserRole)
    # Parcourir les colonnes définies dans MAPING_INVENTORY_POPULATE
    for col in self.JSON.MAPING_INVENTORY_POPULATE:
        if col in inventory_row:
            widget, method, value_transform = self.JSON.MAPING_INVENTORY_POPULATE[col]
            # Transformation de la valeur si nécessaire
            value = value_transform(inventory_row.get(col, ''), liste_name)
            widget_name = widget(inventory_row.get(col, ''), liste_name)
            method_callable = method(inventory_row.get(col, ''), liste_name) if callable(
                method) else method

            # widget
            widget_obj = getattr(dlg, widget_name)
            # Appliquer la méthode spécifiée sur le widget avec la valeur donnée
            method = getattr(widget_obj, method_callable)
            method(value)
            widget_obj.repaint()
            QApplication.processEvents()

            if col == "quantite" and liste_name != "_lw_inventory_list_inventory" and value == 0:
                self.RaiseErreur(widget_obj)

    if liste_name != "_lw_inventory_list_inventory":
        self.maindialog._l_invoice_preview_name.setText(inventory_row.get("nom"))
        self.maindialog._l_invoice_preview_marque.setText(inventory_row.get("marque"))
        self.maindialog._l_invoice_preview_quantity.setText(str(inventory_row.get("quantite")))
        self.maindialog._l_invoice_preview.setScaledContents(False)
        self.maindialog._l_invoiceemptyInventorymess.setVisible(inventory_row.get("quantite") == 0)
        if icon_path := inventory_row.get('icon'):
            pixmap = QPixmap(icon_path)
            if not pixmap.isNull():
                # Mise à l'échelle proportionnelle
                scaled_pixmap = pixmap.scaled(
                    self.maindialog._l_invoice_preview.size(),  # Taille du QLabel
                    Qt.KeepAspectRatio,  # Conserver le ratio
                    Qt.SmoothTransformation  # Transformation douce pour une meilleure qualité
                )
                self.maindialog._l_invoice_preview.setPixmap(scaled_pixmap)
        texte = (QCoreApplication.translate("MainWindow",
                                            u"⚠ Le mat\u00e9riel n'est plus en stock dans le magasin (attente de retour ...)",
                                            None)
                 if inventory_row.get("quantifiable") is True else
                 QCoreApplication.translate("MainWindow",
                                            u"⚠ Le mat\u00e9riel n'est plus en stock dans le magasin (Coninué mais pensez à alimenter le magasin ...)",
                                            None)
                 )
        self.maindialog._l_invoiceemptyInventorymess.setText(texte)
