# Cathal Kelly 18244513
import pygame
import os

class Tank(pygame.sprite.Sprite):
    "The Receiver"
    
    velocity = 12
    
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.image.load(os.path.join('Images/tank.png')).convert()
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        self.change_x = 0
        self.change_y = 0
 
    def update(self):

        self.rect.x += self.change_x
 
    @staticmethod
    def run_move_up_command():
        Tank.rect.y += Tank.velocity
    
    @staticmethod
    def run_move_down_command():
        Tank.rect.y += Tank.velocity
        rect.x = rect.x + 0
        
    @staticmethod
    def run_move_right_command():
        self.rect.x += self.velocity
        self.rect.y = self.rect.y + 0
        
    @staticmethod
    def run_move_left_command():
        Tank.rect.x -= Tank.velocity
        Tank.rect.y = Tank.rect.y + 0
    
    @staticmethod    
    def run_shoot_command():
        print("Executing Shoot Command")    