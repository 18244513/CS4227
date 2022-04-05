# Rioghan Lowry 18226531

import os
import pygame



class Player(pygame.sprite.Sprite):
    
    velocity = 12
    
    def __init__(self, x, y):
        super().__init__()
 
        self.image = pygame.image.load(os.path.join('Images/tank.png')).convert()
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
        
    def update(self):
        
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
    '''
    Cathal
    '''
    
    def run_move_up_command(self):
        self.rect.y -= self.velocity
        self.rect.y = self.rect.y + 0
        
    def run_move_down_command(self):
        self.rect.y += self.velocity
        self.rect.y = self.rect.y - 0
        
    def run_move_right_command(self):
        self.rect.x += self.velocity
        self.rect.x = self.rect.x + 0
        
    def run_move_left_command(self):
        self.rect.x -= self.velocity
        self.rect.x = self.rect.x - 0
    
    @staticmethod    
    def run_shoot_command():
        print("Executing Shoot Command") 
                