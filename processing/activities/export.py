from collections import ChainMap
from copy import deepcopy
from datetime import datetime, timedelta, date
from pathlib import Path

import openpyxl
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from sqlalchemy import distinct, func

from forms.page import populateInvoiceCreatedList
from processing.database.session import WorkSession
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
                        'mail_client' : dlg._le_invoice_mailclient.text(),
                        'tel_client' : dlg._le_invoice_numclient.text(),
                        'objet' : dlg._le_invoice_objet.text(),
                        'validDays' : dlg._s_invoice_validity.value(),
                        "expire": (datetime.today() + timedelta(days=dlg._s_invoice_validity.value())).strftime('%d/%m/%Y'),
                        "today": datetime.today().strftime('%d/%m/%Y'),
                        "id": id
                        }
        self.insertInfo(workbook, worksheet, sauvegarde, info_facture)
        self.insertCommand(workbook, worksheet, sauvegarde, info_facture)
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

    def insertInfo(self, wb: Workbook, ws: Worksheet, sauvegarde: str, info: dict):
        ws["G2"] = str(info.get("id", ""))
        ws["G3"] = str(info.get("today", ""))
        ws["G4"] = str(info.get("expire", ""))
        ws["F7"] = str(info.get("client", ""))
        self.CentrerMultipleCols(wb, ws, "F7:G7", sauvegarde)
        ws["F8"] = f"""✉️ {str(info.get("mail_client", ""))}"""
        self.CentrerMultipleCols(wb, ws, "F8:G8", sauvegarde)
        ws["F9"] = f"""📞 {str(info.get("tel_client", ""))}"""
        self.CentrerMultipleCols(wb, ws, "F9:G9", sauvegarde)
        ws["B11"] = str(info.get("objet", ""))
        ws["B11"].alignment = self.alignerCentrerGauche
        ws.merge_cells("B11:G11")

        wb.save(sauvegarde)

    def insertCommand(self, wb: Workbook, ws: Worksheet, sauvegarde: str, info: dict):
        Liste = self.maindialog._lw_list_cart
        somme = 0
        ORMTable = Devis if self.InvoicePage.lower() == "devis" else Factures
        user = WorkSession.get_current_user()
        with self.Session() as session:
            for i in range(Liste.count()):
                print(i)
                item = Liste.item(i)
                custom_widget = Liste.itemWidget(item)
                if custom_widget:
                    value = custom_widget.getItemInfo
                    print(value.get('type_remise'))
                    ws.append(
                        [
                            value.get('produit'),
                            "",
                            "",
                            value.get('prix_unite'),
                            value.get('quantite'),
                            (
                                value.get('remise')
                                if value.get('type_remise') == "€"
                                else value.get('remise') / 100
                            ),
                            value.get("prix"),
                        ]
                    )
                    # Ligne impaire
                    row = 14 + i
                    for col in range(1, 8):
                        ws.cell(row=row, column=col).alignment = self.alignerCentrer
                        self.BordureExterieur(wb, ws, self.thin, row, row, col, col, sauvegarde)
                        if row % 2 > 0:
                            ws.cell(row, col).fill = openpyxl.styles.PatternFill(
                                start_color="D6F1E8", end_color="D6F1E8", fill_type="solid"
                            )
                        if col in (4, 6, 7):
                            cell = ws.cell(row=row, column=col)
                            if cell and cell.value > 0.0:
                                typeFormat = (
                                    "#,##0.00 €"
                                    if col in (4, 7) or col == 6 and  value.get('type_remise') == "€"
                                    else "0.00 %"
                                )
                                cell.value = float(cell.value)
                                cell.number_format = typeFormat
                                cell.data_type = 'n'
                            else:
                                cell.value = '-'
                    plage = f"A{row}:C{row}"
                    self.CentrerMultipleCols(wb, ws, plage, sauvegarde)


                    somme += float(value.get('prix'))
                    __params = dict(ChainMap(value, info))
                    __params["crea_date"] = date.today()
                    __params["crea_user"] = user.identifiant
                    __params["numero_devis" if self.InvoicePage.lower() == "devis" else "numero_facture"] = f"{__params.get('id')}_{str(i).zfill(2)}"
                    [__params.pop(cle) for cle in ('dlg', 'icon', 'old_price', 'marque','quantifiable', 'louable',
                                                    'validDays', 'expire', 'today')
                    ]
                    print(__params)


        wb.save(sauvegarde)