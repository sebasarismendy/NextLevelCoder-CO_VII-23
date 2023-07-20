from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import POWER_ROBOT


class Robotdino(PowerUp):
    def __init__(self):
        selected_image = POWER_ROBOT
        super().__init__(selected_image)
        self.type = POWER_ROBOT
