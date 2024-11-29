from datetime import datetime

from PySide6.QtCore import QSize, Qt, QDate
from PySide6.QtWidgets import QListWidgetItem

from processing.database.model_public import User, Entreprise
from forms.gui.ui_card_employe import EmployeeCard


class PopulateWidget:

    def populateUserList(self):
        with self.Session() as session:
            user = session.query(
                User.identifiant.label("_le_um_id"),
                User.nom.label("_le_um_nom"),
                User.prenom.label("_le_um_prenom"),
                User.poste.label("_le_um_poste"),
                User.sexe.label("_cbx_um_sexe"),
                User.role.label("_cbx_um_role"),
                User.email.label("_le_um_mail"),
                User.expire.label("_cw_um_expire_account")
                ).order_by(User.nom)
            if user:
                self.maindialog._lw_um_usrList.clear()
                self.maindialog._lw_um_usrList.setStyleSheet("""
                        #_p_user_management #_lw_um_usrList {
                            background-image: none !important;
                        }
                        #_lw_um_usrList::item {
                            background-color: qlineargradient(spread:repeat, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #DDDEFF, stop: 1 #FFFFFF);
                            border: 1px solid rgba(214, 219, 223, 1);
                            border-radius: 8px;
                            margin: 5px;
                        }
                        #_lw_um_usrList::item:hover {
                            border-color: rgba(129, 178, 154, 1);
                        }
                        #_lw_um_usrList::item:selected {
                            border-color: rgba(224, 122, 95, 1);
                        }
                    """)
                for employe in user:
                    card = EmployeeCard(employe)
                    item = QListWidgetItem(self.maindialog._lw_um_usrList)
                    item.setSizeHint(QSize(110, 120))
                    self.maindialog._lw_um_usrList.setItemWidget(item, card)

                    # Store employee info in item data
                    item.setData(Qt.UserRole, employe)
                    # Connect item clicked signal
                    self.maindialog._lw_um_usrList.itemClicked.connect(lambda item: self.populateInputUserList(item.data(Qt.UserRole)))
            else:
                self.maindialog._lw_um_usrList.setStyleSheet(f"""
                        # _p_user_management #_lw_um_usrList {{
                        background - image: url({self.maindialog.user_bg});
                        background - repeat: no - repeat;
                        background - position: center center;
                        background - origin: content;
                    }}"""
                    )

    def populateInputUserList(self, info):
        current_date = QDate.currentDate()
        self.maindialog._cw_um_expire_account.setSelectedDate(current_date)
        for alias, value in info._asdict().items():
            widget = getattr(self.maindialog, alias, None)
            if widget:
                if hasattr(widget, 'setText'):  # Pour QLineEdit
                    widget.setText(str(value))
                elif hasattr(widget, 'setCurrentText'):  # Pour QComboBox
                    widget.setCurrentText(str(value).replace("Employe", "Employé"))
                else:
                    if value and hasattr(widget, 'setSelectedDate'):
                        datetime_obj = datetime.strptime(str(value), "%Y-%m-%d")
                        date_part = datetime_obj.date()
                        widget.setSelectedDate(
                            QDate(date_part.year, date_part.month, date_part.day)
                        )

        self.maindialog._b_um_delete_usr.setEnabled(not (self.USER == info._le_um_id))
        self.maindialog._b_um_update_usr.setEnabled(True)

    def populateInfoCompany(self):
        l = 0
        with self.Session() as session:
            if not self.cacheInfoCompany:
                company = session.query(Entreprise).first()
                self.cacheInfoCompany ={column.name: getattr(company, column.name) for column in Entreprise.__table__.columns}
            if self.cacheInfoCompany:
                companyTable_To_Dlg = {
                    "_le_nom_entreprise": "nom",
                    "_le_nom_dirigeant": "resp_nom",
                    "_le_prenom_dirigeant": "resp_prenom",
                    "_le_nom_rue": "adresse",
                    "_le_ville": "ville",
                    "_le_commune": "commune",
                    "_le_cp": "code_postal",
                    "_le_departement": "departement",
                    "_le_mail": "mail",
                    "_le_num_fixe": "telephone",
                    "_le_num_portable": "portable",
                    "_le_siret": "siret",
                    "_le_siren": "siren",
                    "_le_ape": "code_ape",
                    "_le_iban": "iban",
                    "_le_bic": "bic",
                    "_le_capital": "capital",
                }
                ref = {v: k for k, v in companyTable_To_Dlg.items()}
                l = 1
                for col_name, col_value in self.cacheInfoCompany.items():
                    getattr(self.maindialog, ref[col_name]).setText(str(col_value)
                                                                    if col_value or str(col_value).isdigit()
                                                                    else col_value)

                functions = ["active_valid_entrepise", "active_valid_dirigeant", "active_valid_adresse",
                "active_valid_contact", "active_valid_bank"]
                for func in functions:
                    getattr(self.maindialog, func)()
        return l
