import copy
import openpyxl
from processing.creator.excel import Excel
from processing.creator.plan import ExcelPlans
from processing.creator.model_inventory import ModelImportInventory


class Layout(Excel, ExcelPlans):
    def init_Style(self):
        [
            setattr(self, k, openpyxl.styles.Side(border_style=v))
            for k, v in self.JSON.EXCEL_BORDER_TYPE.items()
        ]
        self.alignement = openpyxl.styles.alignment.Alignment(
            **self.JSON.ALIGNMENT_PARAMS
        )
        self.alignerCentrerDroite = self.addStyleAttribute(
            "alignement",
            {"wrap_text": True, "vertical": "center", "horizontal": "right"},
        )
        self.alignerCentrerGauche = self.addStyleAttribute(
            "alignement",
            {"wrap_text": True, "vertical": "center", "horizontal": "left"},
        )
        self.alignerCentrerHaut = self.addStyleAttribute(
            "alignement", {"wrap_text": True, "vertical": "top", "horizontal": "center"}
        )
        self.alignerCentrer = self.addStyleAttribute(
            "alignement",
            {"wrap_text": True, "vertical": "center", "horizontal": "center"},
        )

    def addStyleAttribute(self, objstyle, attributes):
        s = copy.deepcopy(getattr(self, objstyle))
        for attribut, valeur in attributes.items():
            setattr(s, attribut, valeur)
        return s