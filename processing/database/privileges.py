
from collections import namedtuple
from typing import List, Dict


class PrivilegeManager:
    def __init__(self, maindialog):
        self.maindialog = maindialog
        self.button_names = [
            "dashboard_menu",
            "dashboard_imenu",
            "infoCompany_menu",
            "infoCompany_imenu",
            "workspace_create",
            "workspace_menu",
            "workspace_imenu",
            "manageusers",
            "validfacture",
            "inventory_menu",
            "inventory_imenu",
            "restore_menu",
            "restore_imenu",
            "exportFacture",
        ]

    def get_buttons(self) -> List:
        """
        Récupération des boutons dans les sidebar
        :return: la liste des boutons dans les sidebar
        """
        return [getattr(self.maindialog, name) for name in self.button_names]

    def set_button_states(self, buttons: List, enabled_buttons: List[str]):
        """
        Gérer l'état des boutons
        :param buttons: listes des boutons de la sidebar
        :param enabled_buttons: boutons autorisés à être activés
        :return:
        """
        for button in buttons:
            button.setEnabled(button.objectName() in enabled_buttons)

    def handle_db_login(self, user: str) -> namedtuple:
        """
        Gérer les connexions base de données
        :param user: nom de l'utilisateur'
        :return: nametuple des informations de l'utilisateur
        """
        buttons = self.get_buttons()
        _, nt = self.getUserInfo(user)

        role_permissions: Dict[str, List[str]] = {
            "Administrateur": self.button_names,
            "superutilisateur": self.button_names,
            "Responsable": [
                "validfacture",
                "exportFacture",
                "inventory_menu",
                "inventory_imenu",
            ],
            "Employe": ["exportFacture"],
        }

        enabled_buttons = role_permissions.get(nt.role, self.button_names)
        if self.WorkspaceExist():
            enabled_buttons.remove("workspace_create")

        self.set_button_states(buttons, enabled_buttons)
        return nt

    def handle_guest_login(self):
        """Gérer les connexions invitées"""
        buttons = self.get_buttons()
        allowed_buttons = ["exportFacture"]
        self.set_button_states(buttons, allowed_buttons)
        self.maindialog.dashboard_menu.setEnabled(False)
        self.maindialog.dashboard_imenu.setEnabled(False)
        self.maindialog.dashboard_menu.setChecked(False)
        self.maindialog.dashboard_imenu.setChecked(False)
        self.maindialog.devis.setChecked(True)

    def activePrivileges(self, typeLogin: str = "DB"):
        """
        Activation des privilèges dans le programme selon le type de connexion et le profil
        :param typeLogin: type de connexion du programme -> DB ou Invité
        :return:
        """
        nt = None
        if typeLogin == "DB":
            nt = self.handle_db_login(str(self.USER))
        else:
            self.handle_guest_login()

        self.setup_menu_sidebar(typeLogin, nt)

    def setup_menu_sidebar(self, typeLogin: str, nt):
        """"""
        role = nt.role if typeLogin == "DB" else typeLogin
        for menu_name in ["workspace_imenu", "sold_imenu"]:
            menu = getattr(self.maindialog, menu_name)
            menu.clicked.connect(
                lambda checked, name=menu_name: self.maindialog.visibilityDropright(
                    name, self.WorkspaceExist(), role
                )
            )
