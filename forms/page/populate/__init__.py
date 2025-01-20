from forms.page.populate.user import populateUserList
from forms.page.populate.company import populateInfoCompany
from forms.page.populate.agenda import populateAgenda
from forms.page.populate.clients import populateClientCombo, populateClientTable
from forms.page.populate.database import populateDatabaseExplorer
from forms.page.populate.inventory import populateListInventory
from forms.page.populate.facture import populateInvoiceCreatedList
from forms.page.populate.activites import populateActivList, populateActivitiesTable

__all__ = ["populateUserList", "populateInfoCompany", "populateAgenda", "populateClientCombo", "populateClientTable",
            "populateDatabaseExplorer", "populateListInventory", "populateInvoiceCreatedList", "populateActivList",
            "populateActivitiesTable"]