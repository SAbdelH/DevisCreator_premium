from datetime import datetime
from pathlib import Path

from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from sqlalchemy import distinct, func

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
                        'tel' : dlg._le_invoice_nomclient.text(),
                        'objet' : dlg._le_invoice_objet.text(),
                        'validDays' : dlg._s_invoice_validity.value()
                        }
        self.insertInfo(workbook, worksheet, sauvegarde, info_facture)
        print("fini !")

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
        ws["F7"] = str(info.get("client", ""))
        self.CentrerMultipleCols(wb, ws, "F7:G7", sauvegarde)
        ws["F8"] = str(info.get("mail", ""))
        self.CentrerMultipleCols(wb, ws, "F8:G8", sauvegarde)
        ws["F9"] = str(info.get("tel", ""))
        self.CentrerMultipleCols(wb, ws, "F9:G9", sauvegarde)
        ws["B11"] = str(info.get("objet", ""))
        ws["B11"].alignment = self.alignerCentrerGauche
        ws.merge_cells("B11:G11")
        #self.CentrerMultipleCols(wb, ws, "B11:G11", sauvegarde)
        wb.save(sauvegarde)