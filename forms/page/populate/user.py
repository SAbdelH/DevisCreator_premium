from datetime import datetime

from PySide6.QtCore import QSize, Qt, QDate
from PySide6.QtWidgets import QListWidgetItem

from forms.gui import EmployeeCard
from processing.database.model_public import Ui_Update, User


def populateUserList(self):
    with self.Session() as session:
        self.maindialog._lw_um_usrList.setStyleSheet(f"""
                                    # _p_user_management #_lw_um_usrList {{
                                    background-image: url({self.maindialog.teams_bg});
                                    background-repeat: no - repeat;
                                    background-position: center center;
                                    background-origin: content;
                                }}"""
                                                     )
        update = Ui_Update().verify_update(session, 'user')
        first = self.maindialog.firstOpenUser
        if first:  self.maindialog.ump_last_update = datetime.now().date()

        if first or (update and update.crea_date > self.maindialog.ump_last_update):
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
                    self.maindialog._lw_um_usrList.itemClicked.connect(
                        lambda item: populateInputUserList(self, item.data(Qt.UserRole)))

            self.maindialog.ump_last_update = datetime.now()
            self.maindialog.firstOpenUser = False

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
