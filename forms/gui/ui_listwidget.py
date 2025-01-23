from PySide6.QtWidgets import QListWidget


class CustomListWidget(QListWidget):
    def mousePressEvent(self, event):
        # Vérifier si l'utilisateur a cliqué sur un élément
        item = self.itemAt(event.pos())
        if item is None:  # Si aucun élément n'est cliqué
            self.clearSelection()  # Désélectionner tous les éléments
        super().mousePressEvent(event)  # Assurer le comportement par défaut