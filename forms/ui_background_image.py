import random
from pathlib import Path


class BackgroundImage:
    IGNORE_BACKGROUND_IMAGES = ['analyse', 'camembert', 'evolution', 'histogram',
                                'listActivity', 'table', 'teams', 'ToDo']
    def __init__(self):
        self.arrierePlan = {
            img.stem: img.as_posix()
            for img in Path(Path(__file__).parent).rglob("*")
            if img.suffix in (".png", ".jpeg", ".jpg") and img.parent.stem == 'arriere_plan'
        }

    def RandomBackground(self):
        arrierePlan = {k: v for k, v in self.arrierePlan.items() if k not in self.IGNORE_BACKGROUND_IMAGES}
        randomImg = random.choice(list(arrierePlan))
        self._p_login.setStyleSheet(
            f"border-image: url({arrierePlan[randomImg]}) 0 0 0 0 stretch stretch;"
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