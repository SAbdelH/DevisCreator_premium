import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem

class TaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Task #547 - Contracts')

        main_layout = QVBoxLayout()

        # Création du QTreeWidget
        tree = QTreeWidget()
        tree.setHeaderLabels(['Type', 'Details'])

        # Section Task
        task_item = QTreeWidgetItem(['Task #547', ''])
        task_item.addChild(QTreeWidgetItem(['Contracts', '4']))
        task_item.addChild(QTreeWidgetItem(['Invention Patent', '#2615324']))
        task_item.addChild(QTreeWidgetItem(['Requests', '3']))
        task_item.addChild(QTreeWidgetItem(['Main info', '']))
        tree.addTopLevelItem(task_item)

        # Section Attributes
        attributes_item = QTreeWidgetItem(['Attributes', '4'])
        address_item = QTreeWidgetItem(['Address', ''])
        address_item.addChild(QTreeWidgetItem(['CEO', '']))
        address_item.addChild(QTreeWidgetItem(['Files', '0']))
        address_item.addChild(QTreeWidgetItem(['DB', '2']))
        address_item.addChild(QTreeWidgetItem(['fb', '12']))
        address_item.addChild(QTreeWidgetItem(['a&n', '48']))
        attributes_item.addChild(address_item)
        attributes_item.addChild(QTreeWidgetItem(['Customers', '3']))
        attributes_item.addChild(QTreeWidgetItem(['Orders', '5']))
        tree.addTopLevelItem(attributes_item)

        # Section Recognition Certificate
        recognition_item = QTreeWidgetItem(['Recognition Certificate for Contal...', ''])
        recognition_item.addChild(QTreeWidgetItem(['Act of depot conformity, Bureau...', '']))
        recognition_item.addChild(QTreeWidgetItem(['Chamber of Commerce and India...', '']))
        tree.addTopLevelItem(recognition_item)

        # Section Table (Type)
        type_item = QTreeWidgetItem(['Type', ''])
        type_item.addChild(QTreeWidgetItem(['CEO', '28.09.2023, 15:08:00']))
        type_item.addChild(QTreeWidgetItem(['CEO', '28.09.2023, 15:08:00']))
        type_item.addChild(QTreeWidgetItem(['Address', '28.09.2023, 15:08:00']))
        tree.addTopLevelItem(type_item)

        main_layout.addWidget(tree)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TaskWindow()
    window.show()
    sys.exit(app.exec())