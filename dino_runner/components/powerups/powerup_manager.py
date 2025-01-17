import pygame
import random
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.robotdino import Robotdino
from dino_runner.utils.constants import POWER_ROBOT_TYPE


class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100
        
    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False
                game.player.type = self.powerup.type
                
                if self.powerup.type == POWER_ROBOT_TYPE:
                   print(self.powerup.type)
                   game.game_speed = 60
                self.next_powerup_show = self.generate_next_powerup_show()

    def generate_next_powerup_show(self):
        return random.randint(100, 200)  

    def create_powerup(self):
        powerups = [Shield(), Robotdino()]
        self.powerup = random.choice(powerups)
        self.has_powerup = True

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
        
        font = pygame.font.Font(None, 50)
        text = font.render(f"Next Power-Up Show: {self.next_powerup_show}", True, (255, 255, 255))
        screen.blit(text, (10,10))
