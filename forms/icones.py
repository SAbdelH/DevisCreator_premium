from pathlib import Path

from PyQt6.QtGui import QPixmap
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


class Icones:
    def __init__(self):
        self.images: dict[str, str] = {
            img.stem: img.as_posix()
            for img in Path(Path(__file__).parent).rglob("*")
            if img.suffix in (".png", ".jpeg", ".jpg") and img.parent.stem == 'icons'
        }

    @property
    def entreprise_pixmap_icon(self) -> QPixmap:
        return QPixmap(self.images.get(u"MsCles"))

    @property
    def entreprise_qicon(self) -> QIcon:
        icon: QIcon = QIcon()
        icon.addFile(self.images.get(u"MsCles"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def tableau_de_bord_icon(self) -> QIcon:
        icon: QIcon = QIcon()
        icon.addFile(self.images.get("tableau-de-bord"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def espace_de_travail_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("les-conditions-de-travail"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def gestion_facture_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("facture-dachat"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def gestion_inventaire_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("inventaire"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def gestion_base_de_donnees_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("bases-de-donnees"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    def profil_pixmap(self, img: str = "patron") -> QPixmap:
        return QPixmap(self.images.get(img))

    @property
    def deconnexion_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("sortir"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def logo_connexion_pixmap(self) -> QPixmap:
        return QPixmap(self.images.get("connexion"))

    @property
    def connexion_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("login"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def config_db_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("configBD"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def invite_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("invite"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def retour_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("back"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def logo_config_db_pixmap(self) -> QPixmap:
        return QPixmap(self.images.get("configDB"))

    @property
    def disquette_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("disquette"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def export_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("partager"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def calendrier_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("calendrier"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def activites_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("besoins"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def action_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("lecriture"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

    @property
    def budget_icon(self) -> QIcon:
        icon = QIcon()
        icon.addFile(self.images.get("croissance"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        return icon

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