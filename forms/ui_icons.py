from pathlib import Path

from PyQt6.QtGui import QPixmap
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class Icons:
    def __init__(self):
        self.images: dict[str, str] = {
            img.stem: img.as_posix()
            for img in Path(Path(__file__).parent).rglob("*")
            if img.suffix in (".png", ".jpeg", ".jpg") and img.parent.stem == 'icons'
        }

    def __QIcon(self, img: str) -> QIcon:
        icon: QIcon = QIcon()
        icon.addFile(self.images.get(img), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    def __QPixmap(self, img: str) -> QPixmap:
        return QPixmap(self.images.get(img))

    @property
    def entreprise_pixmap_icon(self) -> QPixmap:
        return self.__QPixmap("MsCles")

    @property
    def entreprise_qicon(self) -> QIcon:
        return self.__QIcon("MsCles")

    @property
    def tableau_de_bord_icon(self) -> QIcon:
        return self.__QIcon("tableau-de-bord")

    @property
    def espace_de_travail_icon(self) -> QIcon:
        return self.__QIcon("les-conditions-de-travail")

    @property
    def gestion_facture_icon(self) -> QIcon:
        return self.__QIcon("facture-dachat")

    @property
    def gestion_inventaire_icon(self) -> QIcon:
        return self.__QIcon("inventaire")

    @property
    def gestion_base_de_donnees_icon(self) -> QIcon:
        return self.__QIcon("bases-de-donnees")

    def profil_pixmap(self, img: str = "patron") -> QPixmap:
        return self.__QPixmap(img)

    @property
    def deconnexion_icon(self) -> QIcon:
        return self.__QIcon("sortir")

    @property
    def logo_connexion_pixmap(self) -> QPixmap:
        return self.__QPixmap("connexion")

    @property
    def connexion_icon(self) -> QIcon:
        return self.__QIcon("login")

    @property
    def config_db_icon(self) -> QIcon:
        return self.__QIcon("configBD")

    @property
    def invite_icon(self) -> QIcon:
        return self.__QIcon("invite")

    @property
    def retour_icon(self) -> QIcon:
        return self.__QIcon("back")

    @property
    def logo_config_db_pixmap(self) -> QPixmap:
        return self.__QPixmap("configDB")

    @property
    def disquette_icon(self) -> QIcon:
        return self.__QIcon("disquette")

    @property
    def export_icon(self) -> QIcon:
        return self.__QIcon("partager")

    @property
    def calendrier_icon(self) -> QIcon:
        return self.__QIcon("calendrier")

    @property
    def activites_icon(self) -> QIcon:
        return self.__QIcon("besoins")

    @property
    def action_icon(self) -> QIcon:
        return self.__QIcon("lecriture")

    @property
    def budget_icon(self) -> QIcon:
        return self.__QIcon("croissance")

    @property
    def plus_icon(self) -> QIcon:
        return self.__QIcon("plus")

    @property
    def ajouter_icon(self) -> QIcon:
        return self.__QIcon("ajouter")

    @property
    def mise_a_jour_icon(self) -> QIcon:
        return self.__QIcon("maj")

    @property
    def supprimer_icon(self) -> QIcon:
        return self.__QIcon("moins")

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
    def pourcentage(self) -> QIcon:
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
    def pdf_file_icon(self) -> QIcon:
        return self.__QIcon("pdfn")

    @property
    def excel_file_icon(self) -> QIcon:
        return self.__QIcon("exceln")

    @property
    def telecharger_icon(self) -> QIcon:
        return self.__QIcon("download")

    @property
    def ajouter_utilisateur_icon(self):
        return self.__QIcon("addclient")

    @property
    def uncheckbox_icon(self) -> str:
        return self.images.get("uncheckedb")

    @property
    def checkbox_icon(self) -> str:
        return self.images.get("checkedb")

    @property
    def opentoolbox_icon(self) -> str:
        return self.images.get("openfolder")

    @property
    def closetoolbox_icon(self) -> str:
        return self.images.get("emptyfolder")