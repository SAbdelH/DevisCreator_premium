import random
from pathlib import Path

IGNORE_BACKGROUND_IMAGES = ['analyse', 'camembert', 'evolution', 'histogram', 'clients', 'inventory',
                                'listActivity', 'table', 'teams', 'ToDo', 'home_bckgnd']

class BackgroundImage:

    def __init__(self):
        self.arrierePlan = {
            img.stem: img.as_posix()
            for img in Path(Path(__file__).parents[1]).rglob("*")
            if img.suffix in (".png", ".jpeg", ".jpg") and img.parent.stem == 'background'
        }

    def RandomBackground(self):
        arrierePlan = {k: v for k, v in self.arrierePlan.items() if k not in IGNORE_BACKGROUND_IMAGES}
        randomImg = random.choice(list(arrierePlan))
        self._p_login.setStyleSheet(
            f"#_p_login {{ border-image: url({arrierePlan[randomImg]}) 0 0 0 0 stretch stretch; }}"
        )

    def home_bg(self):
        self._p_dashboard.setStyleSheet(
            f"#_p_dashboard {{ border-image: url({self.arrierePlan.get('home_bckgnd')}) 0 0 0 0 stretch stretch; }}"
        )

    @property
    def a_faire_bg(self) -> str:
        return self.arrierePlan.get("ToDo")

    @property
    def histogram_bg(self) -> str:
        return self.arrierePlan.get("histogram")

    @property
    def camembert_bg(self) -> str:
        return self.arrierePlan.get("camembert")

    @property
    def evolution_bg(self) -> str:
        return self.arrierePlan.get("evolution")

    @property
    def table_bg(self) -> str:
        return self.arrierePlan.get("table")

    @property
    def activites_bg(self) -> str:
        return self.arrierePlan.get("listActivity")

    @property
    def user_bg(self) -> str:
        return self.arrierePlan.get("teams")

    @property
    def analyse_bg(self) -> str:
        return self.arrierePlan.get("analyse")

    @property
    def clients_bg(self) -> str:
        return self.arrierePlan.get("clients")

    @property
    def inventory_bg(self) -> str:
        return self.arrierePlan.get("inventory")