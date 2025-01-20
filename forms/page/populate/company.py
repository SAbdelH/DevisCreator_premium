from datetime import datetime

from processing.database.model_public import Ui_Update, Entreprise


def populateInfoCompany(self):
    l = 0
    with self.Session() as session:
        update = Ui_Update().verify_update(session, 'company')
        first = self.maindialog.firstOpenFirm
        if first:  self.maindialog.fp_last_update = datetime.now()

        if first or (update and update.crea_date > self.maindialog.fp_last_update):
            company = session.query(Entreprise).first()
            self.cacheInfoCompany = {column.name: getattr(company, column.name) for column in Entreprise.__table__.columns}
            if self.cacheInfoCompany:
                companyTable_To_Dlg = {
                    "_le_nom_entreprise": "nom",
                    "_le_nom_dirigeant": "resp_nom",
                    "_le_prenom_dirigeant": "resp_prenom",
                    "_le_nom_rue": "adresse",
                    "_le_ville": "ville",
                    "_le_commune": "commune",
                    "_le_cp": "code_postal",
                    "_le_departement": "departement",
                    "_le_mail": "mail",
                    "_le_num_fixe": "telephone",
                    "_le_num_portable": "portable",
                    "_le_siret": "siret",
                    "_le_siren": "siren",
                    "_le_ape": "code_ape",
                    "_le_iban": "iban",
                    "_le_bic": "bic",
                    "_le_capital": "capital",
                }
                ref = {v: k for k, v in companyTable_To_Dlg.items()}
                l = 1
                for col_name, col_value in self.cacheInfoCompany.items():
                    getattr(self.maindialog, ref[col_name]).setText(str(col_value)
                                                                    if col_value or str(col_value).isdigit()
                                                                    else col_value)

                functions = ["active_valid_entrepise", "active_valid_dirigeant", "active_valid_adresse",
                             "active_valid_contact", "active_valid_bank"]
                for func in functions:
                    getattr(self.maindialog, func)()
                self.maindialog.fp_last_update = datetime.now().date()
                self.maindialog.firstOpenFirm = False
    return l
