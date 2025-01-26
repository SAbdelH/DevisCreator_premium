from datetime import datetime, timedelta
from pathlib import Path

from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from sqlalchemy import distinct, func

from forms.page import populateInvoiceCreatedList
from processing.enumerations import LevelCritic as LVL
from processing.database.model_public import Devis, Factures


class ActivityExport:
    def exportInvoice(self):
        id = self.getNextID
        workbook: Workbook = Workbook()
        worksheet: Worksheet = workbook.active
        worksheet.title = id
        sauvegarde = Path(self.outputfolder) / self.InvoicePage.capitalize() / f"{self.InvoicePage.lower()}_{id}.xlsx"
        self.ModelFacture(workbook, worksheet, sauvegarde)
        dlg = self.maindialog
        info_facture = {'client' : dlg._le_invoice_nomclient.text(),
                        'mail' : dlg._le_invoice_mailclient.text(),
                        'tel' : dlg._le_invoice_numclient.text(),
                        'objet' : dlg._le_invoice_objet.text(),
                        'validDays' : dlg._s_invoice_validity.value(),
                        "expire": (datetime.today() + timedelta(days=dlg._s_invoice_validity.value())).strftime('%d/%m/%Y'),
                        "today": datetime.today().strftime('%d/%m/%Y'),
                        "id": id
                        }
        self.insertInfo(workbook, worksheet, sauvegarde, info_facture)
        self.maindialog.show_notification(
            f"{sauvegarde.stem} est exporté{'e' if self.InvoicePage == 'Factures' else ''}",
            LVL.success,
        )
        populateInvoiceCreatedList(self)

    @property
    def getNextID(self):
        table = Devis if self.InvoicePage.lower() == 'devis' else Factures
        # Dans votre méthode
        with self.Session() as session:
            currentID = session.query(
                distinct(func.substr(table.numero_devis if self.InvoicePage.lower() == 'devis' else table.numero_facture,
                                    1, 10))
            ).filter(
                func.date_part('month', table.crea_date) == func.date_part('month', func.current_date())
            ).count()
        ID = datetime.today().strftime('%m%Y')
        return f"{ID}{currentID + 1:04}"

    def insertInfo(self, wb, ws, sauvegarde,  info: dict):
        ws["G2"] = str(info.get("id", ""))
        ws["G3"] = str(info.get("today", ""))
        ws["G4"] = str(info.get("expire", ""))
        ws["F7"] = str(info.get("client", ""))
        self.CentrerMultipleCols(wb, ws, "F7:G7", sauvegarde)
        ws["F8"] = f"""✉️ {str(info.get("mail", ""))}"""
        self.CentrerMultipleCols(wb, ws, "F8:G8", sauvegarde)
        ws["F9"] = f"""📞 {str(info.get("tel", ""))}"""
        self.CentrerMultipleCols(wb, ws, "F9:G9", sauvegarde)
        ws["B11"] = str(info.get("objet", ""))
        ws["B11"].alignment = self.alignerCentrerGauche
        ws.merge_cells("B11:G11")

        wb.save(sauvegarde)
