from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QListWidgetItem

from processing.database.model_public import User
from forms.gui.ui_card_employe import EmployeeCard

class PopulateWidget:

    def populateUserList(self):
        with self.Session() as session:
            user = session.query(User)
            if user:
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
        print(info)