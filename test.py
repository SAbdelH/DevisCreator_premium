from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QStyledItemDelegate
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt


class CustomDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        """
        Peinture personnalisée avec un fond arrondi seulement pour la colonne 5.
        """
        painter.save()

        # Vérifier si la colonne est la 5
        if index.column() == 5:
            text = index.data()  # Récupérer le texte de la cellule
            if text:
                # Couleur de texte en fonction de la valeur
                if text == "ACCEPTED":
                    text_color = QColor("green")
                elif text == "PENDING":
                    text_color = QColor("orange")
                elif text == "OVERDUE":
                    text_color = QColor("red")
                else:
                    text_color = QColor("black")

                # Configurer les dimensions du texte
                painter.setFont(option.font)
                text_rect = painter.boundingRect(option.rect, Qt.AlignCenter, text)

                # Dessiner le fond arrondi autour du texte
                painter.setBrush(QBrush(QColor(242, 243, 244)))  # Fond gris clair
                painter.setPen(Qt.NoPen)
                margin = 4  # Marges autour du texte
                text_rect.adjust(-margin, -margin, margin, margin)  # Étendre le rectangle
                corner_radius = 8  # Rayon des coins arrondis
                painter.drawRoundedRect(text_rect, corner_radius, corner_radius)

                # Dessiner le texte avec la couleur correcte
                painter.setPen(QPen(text_color))
                painter.drawText(option.rect, Qt.AlignCenter, text)
        else:
            # Rendu standard pour les autres colonnes
            super().paint(painter, option, index)

        painter.restore()


def setup_table(table_widget):
    # Définir le nombre de colonnes
    table_widget.setColumnCount(7)
    table_widget.setHorizontalHeaderLabels(["Sent Date", "Documents", "Associated Project",
                                            "Value", "Balance Due", "Status", "Due Date"])

    # Ajouter des lignes avec des données
    data = [
        ["10/11/2022", "Estimate #001006", "Dr Emmet Brown - Kids Bath", "$2,080", "$6,099", "ACCEPTED", "10/12/2022"],
        ["10/11/2022", "Estimate #001006", "Faruk's Bathroom Remodel", "$2,080", "$6,099", "PENDING", "10/12/2022"],
        ["10/11/2022", "Estimate #001006", "Selim's Washroom Rework", "$2,080", "$6,099", "OVERDUE", "10/12/2022"],
    ]

    for row_index, row_data in enumerate(data):
        table_widget.insertRow(row_index)
        for col_index, value in enumerate(row_data):
            item = QTableWidgetItem(value)

            # Appliquer un style personnalisé pour la 6ème colonne (Status)
            if col_index == 5:
                if value == "ACCEPTED":
                    item.setForeground(QColor("green"))  # Texte en vert
                elif value == "PENDING":
                    item.setForeground(QColor("orange"))  # Texte en orange
                elif value == "OVERDUE":
                    item.setForeground(QColor("red"))  # Texte en rouge

            table_widget.setItem(row_index, col_index, item)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    table_widget = QTableWidget()
    table_widget.setRowCount(0)
    setup_table(table_widget)

    # Appliquer le délégué personnalisé
    delegate = CustomDelegate()
    table_widget.setItemDelegate(delegate)

    table_widget.resize(800, 300)
    table_widget.show()
    sys.exit(app.exec_())