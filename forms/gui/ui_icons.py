from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap


class Icons:
    def __init__(self):
        self.images: dict[str, str] = {
            img.stem: img.as_posix()
            for img in Path(Path(__file__).parents[1]).rglob("*")
            if img.suffix in (".png", ".jpeg", ".jpg") and img.parent.stem == 'icons'
        }

    def __QIcon(self, img: str) -> QIcon:
        """
        Création d'un QIcon simplifier à partir de la bibliothèque d'images
        :param img: Nom de l'image
        :return: un QIcon
        """
        path = self.images.get(img)
        if not path or not Path(path).exists():
            return QIcon()  # Retourne un QIcon vide en cas d'erreur
        icon: QIcon = QIcon()
        icon.addFile(path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    def __QPixmap(self, img: str) -> QPixmap:
        """
        Création d'un QPixmap simplifier à partir de la bibliothèque d'images
        :param img: Nom de l'image
        :return: un QPixmap
        """
        return QPixmap(self.images.get(img))

    @property
    def entreprise_pixmap_icon(self) -> QPixmap:
        """
        Un pixmap de l'icon de l'entreprise
        :return: un QPixmap
        """
        return self.__QPixmap("company")

    @property
    def entreprise_qicon(self) -> QIcon:
        """
        Un QIcon de l'icon de l'entreprise
        :return: un QIcon
        """
        return self.__QIcon("company")

    @property
    def cadena_icon(self) -> QIcon:
        """
        Un QIcon de l'icon cadena
        :return: un QIcon
        """
        return self.__QIcon("cadena")

    @property
    def cle_icon(self) -> QIcon:
        """
        Un QIcon de l'icon cle
        :return: un QIcon
        """
        return self.__QIcon("cle")

    @property
    def utilisateur_icon(self) -> QIcon:
        """
        Un QIcon de l'icon cle
        :return: un QIcon
        """
        return self.__QIcon("utilisateur")

    @property
    def tableau_de_bord_icon(self) -> QIcon:
        """
        Un QIcon de l'icon de tableau de bord
        :return: un QIcon
        """
        return self.__QIcon("tableau-de-bord")

    @property
    def espace_de_travail_icon(self) -> QIcon:
        """
        Un QIcon de l'icon espace de travail
        :return: un QIcon
        """
        return self.__QIcon("les-conditions-de-travail")

    @property
    def gestion_facture_icon(self) -> QIcon:
        """
        Un QIcon de l'icon gestion facture
        :return: un QIcon
        """
        return self.__QIcon("facture-dachat")

    @property
    def gestion_inventaire_icon(self) -> QIcon:
        """
        Un QIcon de l'icon gestion des inventaires
        :return: un QIcon
        """
        return self.__QIcon("inventaire")

    @property
    def gestion_base_de_donnees_icon(self) -> QIcon:
        """
        Un QIcon de l'icon gestion de base de donnees
        :return:
        """
        return self.__QIcon("bases-de-donnees")

    def profil_pixmap(self, img: str = "Administrateur_Homme") -> QPixmap:
        """
        Un pixmap de l'image profil
        :param img: nom du profil
        :return: un QPixmap
        """
        return self.__QPixmap(img)

    @property
    def deconnexion_icon(self) -> QIcon:
        """
        Un QIcon de l'icon deconnexion
        :return: un QIcon
        """
        return self.__QIcon("sortir")

    @property
    def logout_icon(self) -> QIcon:
        return self.__QIcon("logout")

    @property
    def dark_mode_icon(self) -> QIcon:
        return self.__QIcon("dark-mode")

    @property
    def white_mode_icon(self) -> QIcon:
        return self.__QIcon("white-mode")

    @property
    def help_center_icon(self) -> QIcon:
        return self.__QIcon("helps")

    @property
    def abonnement_basic_icon(self) -> QIcon:
        return self.__QIcon("basic")

    @property
    def abonnement_premium_icon(self) -> QIcon:
        return self.__QIcon("premium")

    @property
    def abonnement_invite_icon(self) -> QIcon:
        return self.__QIcon("free")

    @property
    def software_upgrade_icon(self) -> QIcon:
        return self.__QIcon("softupdate")

    @property
    def reglage_icon(self) -> QIcon:
        return self.__QIcon("setting")

    @property
    def logo_connexion_pixmap(self) -> QPixmap:
        """
        Un pixmap de l'icon logo connexion
        :return: un QPixmap
        """
        return self.__QPixmap("connexion")

    @property
    def connexion_icon(self) -> QIcon:
        """
        Un QIcon de l'icon connexion
        :return: un QIcon
        """
        return self.__QIcon("login")

    @property
    def config_db_icon(self) -> QIcon:
        """
        Un QIcon de l'icon config bd
        :return: un QIcon
        """
        return self.__QIcon("configBD")

    @property
    def invite_icon(self) -> QIcon:
        """
        Un QIcon de l'icon invite
        :return: un QIcon
        """
        return self.__QIcon("invite")

    @property
    def retour_icon(self) -> QIcon:
        """
        Un QIcon de l'icon retour
        :return: un QIcon
        """
        return self.__QIcon("back")

    @property
    def logo_config_db_pixmap(self) -> QPixmap:
        """
        Un pixmap de l'icon logo config db
        :return: un QPixmap
        """
        return self.__QPixmap("configBD")

    @property
    def disquette_icon(self) -> QIcon:
        """
        Un QIcon de l'icon disquette de sauvegarde
        :return: un QIcon
        """
        return self.__QIcon("disquette")

    @property
    def export_icon(self) -> QIcon:
        """
        Un QIcon de l'icon export
        :return: un QIcon
        """
        return self.__QIcon("partager")

    @property
    def calendrier_icon(self) -> QIcon:
        """
        Un QIcon de l'icon calendrier
        :return: un QIcon
        """
        return self.__QIcon("calendrier")

    @property
    def activites_icon(self) -> QIcon:
        """
        Un QIcon de l'icon activites
        :return: un QIcon
        """
        return self.__QIcon("besoins")

    @property
    def action_icon(self) -> QIcon:
        """
        Un QIcon de l'icon action
        :return: un QIcon
        """
        return self.__QIcon("lecriture")

    @property
    def budget_icon(self) -> QIcon:
        """
        Un QIcon de l'icon budget
        :return: un QIcon
        """
        return self.__QIcon("croissance")

    @property
    def plus_icon(self) -> QIcon:
        """
        Un QIcon de l'icon plus
        :return: un QIcon
        """
        return self.__QIcon("plus")

    @property
    def ajouter_icon(self) -> QIcon:
        """
        Un QIcon de l'icon ajouter
        :return: un QIcon
        """
        return self.__QIcon("ajouter")

    @property
    def mise_a_jour_icon(self) -> QIcon:
        """
        Un QIcon de l'icon mise a jour
        :return: un QIcon
        """
        return self.__QIcon("maj")

    @property
    def supprimer_icon(self) -> QIcon:
        """
        Un QIcon de l'icon moins
        :return:
        """
        return self.__QIcon("moins")

    @property
    def backspace_icon(self) -> QIcon:
        """
        Un QIcon de l'icon supprimer
        :return:
        """
        return self.__QIcon("supprimer")

    @property
    def valid_icon(self) -> QIcon:
        return self.__QIcon("ui_valid")

    @property
    def homme_icon(self) -> QIcon:
        return self.__QIcon("homme")

    @property
    def femme_icon(self) -> QIcon:
        return self.__QIcon("femme")

    @property
    def admin_icon(self) -> QIcon:
        return self.__QIcon("admin")

    @property
    def responsable_icon(self) -> QIcon:
        return self.__QIcon("respons")

    @property
    def employee_icon(self) -> QIcon:
        return self.__QIcon("employe")

    @property
    def euro_icon(self) -> QIcon:
        return self.__QIcon("euro")

    @property
    def pourcentage_icon(self) -> QIcon:
        return self.__QIcon("pour-cent")

    @property
    def annuler_icon(self) -> QIcon:
        return self.__QIcon("annuler")

    @property
    def commande_icon(self) -> QIcon:
        return self.__QIcon("commande-en-ligne")

    @property
    def excel_icon(self) -> QIcon:
        return self.__QIcon("exceller")

    @property
    def pdf_icon(self) -> QIcon:
        return self.__QIcon("pdf")

    @property
    def pdf_file_pixmap(self) -> QPixmap:
        return self.__QPixmap("pdfn")

    @property
    def excel_file_pixmap(self) -> QPixmap:
        return self.__QPixmap("exceln")

    @property
    def telecharger_icon(self) -> QIcon:
        return self.__QIcon("download")

    @property
    def ajouter_utilisateur_icon(self):
        return self.__QIcon("addclient")

    @property
    def profil_client_icon(self) -> QIcon:
        return self.__QIcon("profilClient")

    @property
    def achat_icon(self) -> QIcon:
        return self.__QIcon("achat")

    @property
    def profil_client_pixmap(self) -> QPixmap:
        return self.__QPixmap("profilClient")

    @property
    def mail_client_icon(self) -> QIcon:
        return self.__QIcon("e-mail")

    @property
    def mail_client_pixmap(self) -> QPixmap:
        return self.__QPixmap("e-mail")

    @property
    def copier_icon(self) -> QIcon:
        return self.__QIcon("copier")

    @property
    def telephone(self) -> QIcon:
        return self.__QIcon("appel")

    @property
    def telephone_pixmap(self) -> QPixmap:
        return self.__QPixmap("appel")

    @property
    def cacher_widget_icon(self) -> QIcon:
        return self.__QIcon("cacher")

    @property
    def corbeil_icon(self) -> QIcon:
        return self.__QIcon("effacer")

    @property
    def plus_vendu_pixmap(self) -> QPixmap:
        return self.__QPixmap("most_sell")

    @property
    def total_vente_pixmap(self) -> QPixmap:
        return self.__QPixmap("sum_sell")

    @property
    def moins_vendu_pixmap(self) -> QPixmap:
        return self.__QPixmap("low_sell")

    @property
    def restore_icon(self) -> QIcon:
        return self.__QIcon("RESTORE")

    @property
    def logo_backup_pixmap(self) -> QPixmap:
        return self.__QPixmap("nuage")

    @property
    def create_ws_icon(self) -> QIcon:
        return self.__QIcon("workspace")

    @property
    def create_users_icon(self) -> QIcon:
        return self.__QIcon("adduser")

    @property
    def informations_entreprise_icon(self) -> QIcon:
        return self.__QIcon("entreprise")

    @property
    def create_devis_icon(self) -> QIcon:
        return self.__QIcon("devis")

    @property
    def create_facture_icon(self) -> QIcon:
        return self.__QIcon("facture")

    @property
    def create_client_icon(self) -> QIcon:
        return self.__QIcon("client")

    @property
    def create_backup_icon(self) -> QIcon:
        return self.__QIcon("sauvegarde")

    @property
    def valid_facture_icon(self) -> QIcon:
        return self.__QIcon("validFacture")

    @property
    def manage_db_icon(self) -> QIcon:
        return self.__QIcon("manageBD")

    @property
    def combo_facture_icon(self) -> QIcon:
        return self.__QIcon("facturen")

    @property
    def combo_bon_livraison_icon(self) -> QIcon:
        return self.__QIcon("bon-de-livraison")

    @property
    def uncheckbox_icon(self) -> str:
        return self.images.get("uncheckedb")

    @property
    def checkbox_icon(self) -> str:
        return self.images.get("checkedb")

    @property
    def dropdownComboButton_icon(self) -> str:
        return self.images.get("dropdown")

    @property
    def upChevron_icon(self) -> str:
        return self.images.get("up-chevron")

    @property
    def downChevron_icon(self) -> str:
        return self.images.get("down-chevron")

    @property
    def opentoolbox_icon(self) -> str:
        return self.images.get("openfolder")

    @property
    def closetoolbox_icon(self) -> str:
        return self.images.get("emptyfolder")

    @property
    def ientreprise_pixmap(self) -> QPixmap:
        return self.__QPixmap("ientreprise")

    @property
    def iadresse_pixmap(self) -> QPixmap:
        return self.__QPixmap("iadresse")

    @property
    def reflexion_pixmap(self) -> QPixmap:
        return self.__QPixmap("think")

    @property
    def ibank_pixmap(self) -> QPixmap:
        return self.__QPixmap("ibank")

    @property
    def icompany_pixmap(self) -> QPixmap:
        return self.__QPixmap("icompany")

    @property
    def icontact_pixmap(self) -> QPixmap:
        return self.__QPixmap("icontact")

    @property
    def isiren_pixmap(self) -> QPixmap:
        return self.__QPixmap("isiren")

    @property
    def idirigeant_pixmap(self) -> QPixmap:
        return self.__QPixmap("idirigeant")

    @property
    def insee_pixmap(self) -> QPixmap:
        return self.__QPixmap("insee")

    @property
    def eye_closed_icon(self) -> QIcon:
        return self.__QIcon("closeeye")

    @property
    def eye_open_icon(self) -> QIcon:
        return self.__QIcon("openeye")

    @property
    def database_table(self) -> QIcon:
        return self.__QIcon("tableau")