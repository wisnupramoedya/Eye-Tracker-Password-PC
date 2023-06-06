import random
from typing import List

class MaterialIcon:
    icon_name: str
    icon_code: str

    def __init__(self, icon_name: str, icon_code: str) -> None:
        self.icon_name = icon_name
        self.icon_code = icon_code

material_icon_codes: List[MaterialIcon] = [
    MaterialIcon('Undo', 'mdi6.undo'),
    MaterialIcon('Apps', 'mdi6.apps'),
    MaterialIcon('Autorenew', 'mdi6.autorenew'),
    MaterialIcon('Home', 'mdi6.home'),
    MaterialIcon('Delete', 'mdi6.delete'),
    MaterialIcon('Cancel', 'mdi6.cancel'),
    MaterialIcon('Curtains', 'mdi6.curtains'),
    MaterialIcon('Caravan', 'mdi6.caravan'),
    MaterialIcon('Carrot', 'mdi6.carrot'),
    MaterialIcon('Eject', 'mdi6.eject'),
    MaterialIcon('Spear', 'mdi6.spear'),
    MaterialIcon('Shield', 'mdi6.shield'),
    MaterialIcon('Sony PS', 'mdi6.sony-playstation'),
    MaterialIcon('Forest', 'mdi6.forest'),
    MaterialIcon('Muffin', 'mdi6.muffin'),
    MaterialIcon('Anchor', 'mdi6.anchor')
]


class Icons:
    @staticmethod
    def generate_random_icon() -> List[MaterialIcon]:
        randomized_icon = material_icon_codes.copy()
        random.shuffle(randomized_icon)
        return randomized_icon
