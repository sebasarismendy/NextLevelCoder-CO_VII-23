import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
import random


class ObstacleManager:

    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
        if self.obstacle.rect.x > 0:
            self.has_obstacle = True
       
        else:
            self.has_obstacle = False
        self.obstacle.update(game.game_speed)
        
        if game.player.rect.colliderect(self.obstacle.rect):
            pygame.time.delay(400)
            game.playing = False

    def create_obstacle(self):
        obstacle_list = [Cactus(), Bird()]
        self.obstacle = random.choice(obstacle_list)

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)
