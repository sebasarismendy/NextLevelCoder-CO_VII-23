import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants  import (
    RUNNING,
    DUCKING,
    JUMPING
)

class Dinosaur(Sprite):
    
    #constantes
    pos_x = 80
    pos_y = 300
    duck_pos_y = 340
    jumping_vel = 8.5
    
  #insertamos los sprite que son las imagenes del dino
    def __init__(self):
         self.image = RUNNING[0]
         self.rect = self.image.get_rect()
         self.rect.x = self.pos_x
         self.rect.y = self.pos_y
         self.step_index = 0
         self.running = True
         self.ducking = False
         self.jumping = False
         self.jumping_velocity = self.jumping_vel
         
         
    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        print(self.jumping)
        
        if user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] or user_input[pygame.K_w] or user_input[pygame.K_SPACE]:
            self.running = False
            self.ducking = False 
            self.jumping = True
        
        elif not self.jumping:
           self.running = True
           self.ducking = False
           self.jumping = False
        
        if self.step_index >= 10:
            self.step_index = 0
   
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.step_index += 1
    
    def jump(self):
        self.image = JUMPING
        if self.jumping:
            self.rect.y -= self.jumping_velocity *4
            self.jumping_velocity -= 0.8 #cuando es negativo empieza a decender
        
        if self.jumping_velocity < -self.jumping_vel:
            self.rect.y = self.pos_y
            self.jumping = False
            self.jumping_velocity = self.jumping_vel
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index <5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.duck_pos_y
        self.step_index += 1
        

         
     