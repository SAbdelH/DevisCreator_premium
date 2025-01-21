from collections import namedtuple
from datetime import datetime, date

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QListWidgetItem
from sqlalchemy import text, func, and_

from forms.gui import AgendaItem
from processing.database.model_public import Ui_Update, Agenda
from processing.database.session import WorkSession


def populateAgenda(self):
    dlg = self.maindialog
    with (self.Session() as session):
        update = Ui_Update().verify_update(session, 'agenda',
                                        filtre=Ui_Update.crea_user == WorkSession.get_current_user().identifiant)
        first = self.maindialog.firstOpenDashboard
        if first:  self.maindialog.agenda_last_update = datetime.now()

        if first or (update and update.crea_date > self.maindialog.agenda_last_update):
            dlg._lw_agenda.clear()
            session.execute(text("SET lc_time TO 'fr_FR.UTF-8';"))
            agenda = (
                session.query(
                    Agenda.id,
                    Agenda.titre,
                    Agenda.description,
                    func.substr(func.to_char(Agenda.jour, 'TMDay'), 1, 3).label('day'),
                    func.to_char(Agenda.jour, 'dd').label('day_number'),
                    func.concat(
                        func.to_char(Agenda.heure_debut, 'HH24:MI'),
                        ' - ',
                        func.to_char(Agenda.heure_fin, 'HH24:MI')
                    ).label('delay'),
                    Agenda.heure_debut,
                    Agenda.jour,
                    Agenda.heure_fin,
                    func.to_char(Agenda.jour, 'dd-mm-yyyy').label('fjour')
                )
                .filter(
                    and_(
                        func.to_char(Agenda.jour, 'mm/yyyy') >= func.to_char(date.today(), 'mm/yyyy'),
                        Agenda.crea_user == func.current_user()
                    )
                )
            )

            if agenda.count() > 0:
                # Ajout des widgets personnalisés à la liste
                for row, rdv in enumerate(agenda):
                    info = {
                        'id': rdv.id,
                        'titre': rdv.titre,
                        'description': rdv.description,
                        'heure_debut': rdv.heure_debut,
                        'day': f"{rdv.day}.",
                        'day_number': rdv.day_number,
                        'delay': rdv.delay,
                        'jour': rdv.jour,
                        'heure_fin': rdv.heure_fin,
                        'fjour': rdv.fjour
                    }
                    infos = namedtuple("info", info.keys())(*info.values())
                    self.agendaID[row] = info
                    item = QListWidgetItem(dlg._lw_agenda)
                    custom_widget = AgendaItem(infos)  # Crée un widget personnalisé pour l'élément

                    # Ajouter les données au QListWidgetItem
                    item.setData(Qt.UserRole, info)  # Associer les données à l'item

                    item.setSizeHint(QSize(custom_widget.width(), 80))  # Ajuste la taille de l'item selon le widget
                    dlg._lw_agenda.addItem(item)
                    dlg._lw_agenda.setItemWidget(item, custom_widget)

            self.maindialog.agenda_last_update = datetime.now().date()

        dlg._lw_agenda.itemClicked.connect(lambda item: onAgendaItemSelected(self, item))
        dlg._lw_agenda.scrollToBottom()

def onAgendaItemSelected(self, item):
    dlg = self.maindialog
    agenda_row = item.data(Qt.UserRole)

    titre = agenda_row.get("titre")
    description = agenda_row.get("description")
    jour = agenda_row.get("jour")
    heure_debut = agenda_row.get("heure_debut")
    heure_fin = agenda_row.get("heure_fin")

    dlg._le_titre_agenda.setText(titre)
    dlg._le_description.setText(description)

    dlg._de_jour_agenda.setDate(jour)
    dlg._cw_agenda.setSelectedDate(jour)
    dlg._te_debut_agenda.setTime(heure_debut)
    dlg._te_fin_agenda.setTime(heure_fin)
