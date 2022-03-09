import os
from pdb import main
import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
 
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
        
        
        
        print('x = ' + str(self.rect.left))
        print('y = ' + str(self.rect.top))
 
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
Wall Class
'''
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        
        super().__init__()
 
 
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
 
pygame.init()
 
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
 
pygame.display.set_caption('Tank Trouble')
 
 
all_sprite_list = pygame.sprite.Group()
 
'''
Walls
'''
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
 
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
'''
Rotate tank 
'''
tank_up = pygame.transform.rotate(player.image, 0)
tank_left = pygame.transform.rotate(player.image, 90)
tank_down = pygame.transform.rotate(player.image, 180)
tank_right = pygame.transform.rotate(player.image, 270)
 
while main:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
                player.image = tank_left
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
                player.image = tank_right
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
                player.image = tank_up
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)
                player.image = tank_down
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player.changespeed(0, -3)
                
        if pygame.key.get_pressed()[pygame.K_q]:
            quit()
            

        
 
    all_sprite_list.update()
    
    background = pygame.image.load("Images/grass.png")
    screen.blit(background, (0, 0))
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()