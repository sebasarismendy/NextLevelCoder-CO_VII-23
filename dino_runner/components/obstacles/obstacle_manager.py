import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.mike import Mike
from dino_runner.components.obstacles.fireball import Fire 
import random

from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, POWER_ROBOT_TYPE

class ObstacleManager:

    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)
        if game.player.rect.colliderect(self.obstacle.rect):
            if game.player.type == SHIELD_TYPE:
                game.player.type = DEFAULT_TYPE
                self.has_obstacle = False
                
            elif game.player.type == POWER_ROBOT_TYPE:
                pygame.time.delay(1000)
                game.game_speed = 20
                game.player.type = DEFAULT_TYPE
                self.has_obstacle = False

            else:
                pygame.time.delay(400)
                game.playing = False
        
            
    def create_obstacle(self):
        obstacle_list = [Cactus(), Bird(),Mike(),Fire()]
        self.obstacle = random.choice(obstacle_list)

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)
