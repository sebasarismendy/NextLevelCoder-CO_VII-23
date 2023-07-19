import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import Mk


class Mike(Obstacle):
    def __init__(self):
        image = Mk
        super().__init__(image)
        self.rect.y = 300