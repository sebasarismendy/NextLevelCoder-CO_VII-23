from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird (Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = 250
        self.counter = 0
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        self.counter += 1
        self.image = BIRD[0] if self.counter %4 else BIRD[1] 