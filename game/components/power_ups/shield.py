from game.components.power_ups.power_up import PowerUps
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUps):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)