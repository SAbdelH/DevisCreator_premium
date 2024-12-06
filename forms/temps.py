from PySide6.QtCore import QDate, QTime

class TempsForm:
    def aujourdhui(self):
        current_date = QDate.currentDate()
        current_time = QTime.currentTime()
        self._de_jour_agenda.setDate(current_date)
        self._de_inventory_fabric.setDate(current_date)
        self._te_debut_agenda.setTime(current_time)
        self._te_fin_agenda.setTime(current_time.addSecs(30 * 60))

    def dateSelected(self):
        selected_date = self._cw_agenda.selectedDate()
        current_time = QTime.currentTime()
        self._de_jour_agenda.setDate(selected_date)
        self._te_debut_agenda.setTime(current_time)
        self._te_fin_agenda.setTime(current_time.addSecs(3600))