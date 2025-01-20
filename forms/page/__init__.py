from forms.page.interfaces.login import LoginPage as LP
from forms.page.interfaces.dashboard import DashboardPage as DP
from forms.page.interfaces.company import firmPage as FP
from forms.page.interfaces.user import UserManagementPage as UMP
from forms.page.interfaces.facture import InvoicePage as IP
from forms.page.interfaces.validfacture import validFacturePage as VFP
from forms.page.interfaces.clients import clientsPage as CP
from forms.page.interfaces.inventory import InventoryPage as MP # Material Page
from forms.page.interfaces.restoration import restorePage as RP
from forms.page.interfaces.database import DbManagementPage as DMP
from forms.page.populate import *

__all__ = ["LP", "DP", "FP", "UMP", "IP", "VFP", "CP", "MP", "RP", "DMP"]
