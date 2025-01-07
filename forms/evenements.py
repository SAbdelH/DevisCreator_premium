from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import Signal, QObject, QEvent, Qt


class KeyPressFilter(QObject):
    # Signal qui enverra les éléments supprimés
    itemsDeleted = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, event):
        # Si un événement clavier est détecté
        if event.type() == QEvent.KeyPress and (
            event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace
        ):
            if isinstance(obj, QListWidget):
                # Collecter les éléments sélectionnés à supprimer avec leurs index
                deleted_items = [obj.row(item) + 1 for item in obj.selectedItems()]
                [obj.takeItem(obj.row(item)) for item in obj.selectedItems()]
                # Émettre un signal avec les éléments supprimés
                self.itemsDeleted.emit(deleted_items)
            return True  # Événement traité
        return super().eventFilter(obj, event)