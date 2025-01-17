from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import fire

class Fire (Obstacle):
    def __init__(self):
        self.image = fire[0]
        super().__init__(self.image)
        self.rect.y = 270
        self.counter = 0
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        self.counter += 1
        self.image = fire[0] if self.counter %6 else fire[1] 