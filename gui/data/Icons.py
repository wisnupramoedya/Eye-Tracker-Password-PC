import random
from typing import List


class Icons:
    material_icon_codes: List[str] = [
        'mdi6.undo',
        'mdi6.apps',
        'mdi6.autorenew',
        'mdi6.home',
        'mdi6.delete',
        'mdi6.cancel',
        'mdi6.curtains',
        'mdi6.caravan',
        'mdi6.carrot',
        'mdi6.eject',
        'mdi6.spear',
        'mdi6.shield',
        'mdi6.sony-playstation',
        'mdi6.forest',
        'mdi6.muffin',
        'mdi6.anchor',
        'mdi6.transcribe',
        'mdi6.storefront',
        'mdi6.gas-cylinder',
        'mdi6.gift-open-outline',
        'mdi6.ghost',
        'mdi6.ocarina',
        'mdi6.golf-cart',
        'mdi6.google-downasaur',
        'mdi6.panda'
    ]

    randomized_icon: List[str]

    def __init__(self):
        self.generate_random_icon()

    def generate_random_icon(self):
        self.randomized_icon = self.material_icon_codes.copy()
        random.shuffle(self.randomized_icon)
