import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    DUCKING_SHIELD,
    
    POWER_ROBOT_DUCK,
    POWER_ROBOT_JUMP,
    POWER_ROBOT_RUN,
    POWER_ROBOT_TYPE,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    RUNNING,
    DUCKING,
    JUMPING,
    DEFAULT_TYPE,
    SHIELD_TYPE
)

class Dinosaur(Sprite):
    
    POS_X = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.running_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, POWER_ROBOT_TYPE: POWER_ROBOT_RUN}
        self.jumping_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, POWER_ROBOT_TYPE: POWER_ROBOT_JUMP}
        self.ducking_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, POWER_ROBOT_TYPE: POWER_ROBOT_DUCK}
        
        self.type = DEFAULT_TYPE

        self.image = self.running_img[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VEL
        self.setup_states()

    def setup_states(self):
        self.has_powerup = False
        self.has_shield = False
        self.has_power_robot = False
        
        
    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] and not self.jumping:
            self.running = False
            self.ducking = False
            self.jumping = True
            pygame.mixer.music.play

            
            
        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False
            
        if self.step_index >= 10:
            self.step_index = 0
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def run(self):
        self.image = self.running_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jumping_img [self.type]
        if self.jumping:
            self.rect.y -= self.jumping_velocity * 4
            self.jumping_velocity -= 0.8
        if self.jumping_velocity < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VEL

    def duck(self):
        self.image = self.ducking_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCK_POS_Y    
        
        self.step_index += 1
        
         
     
     