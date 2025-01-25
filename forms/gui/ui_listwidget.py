from PySide6.QtWidgets import QListWidget


class CustomListWidget(QListWidget):
    def mousePressEvent(self, event):
        # Vérifier si l'utilisateur a cliqué sur un élément
        item = self.itemAt(event.pos())
        if item is None:  # Si aucun élément n'est cliqué
            self.clearSelection()  # Désélectionner tous les éléments
        else:  # Si un élément est cliqué
            self.setCurrentItem(item)  # S'assurer que l'élément est sélectionné
        self.refresh_items()  # Forcer la mise à jour des styles visuels
        super().mousePressEvent(event)  # Assurer le comportement par défaut

    def refresh_items(self):
        """Forcer la mise à jour de tous les items visibles pour gérer les changements visuels."""
        for i in range(self.count()):
            item = self.item(i)
            rect = self.visualItemRect(item)  # Obtenir la zone visible de l'item
            self.viewport().update(rect)  # Forcer le rafraîchissement
