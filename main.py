# Rioghan Lowry 18226531

from pdb import main
import pygame
import contextObject
from wall import Wall
from dispatcher import Dispatcher
 
pygame.init()
pygame.display.set_caption('Tank Trouble')
all_sprite_list = pygame.sprite.Group()
 
'''
Walls
'''
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 780, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 200, 500, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(700, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 

contextObject.player.walls = wall_list

all_sprite_list.add(contextObject.player)
 
clock = pygame.time.Clock()
 
'''
Rotate tank 
'''
tank_up = pygame.transform.rotate(contextObject.player.image, 0)
tank_left = pygame.transform.rotate(contextObject.player.image, 90)
tank_down = pygame.transform.rotate(contextObject.player.image, 180)
tank_right = pygame.transform.rotate(contextObject.player.image, 270)     

 
while main:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()      

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                contextObject.player.changespeed(-3, 0)
                contextObject.player.image = tank_left
                
            elif event.key == pygame.K_d:
                contextObject.player.changespeed(3, 0)
                contextObject.player.image = tank_right
                
            elif event.key == pygame.K_w:
                contextObject.player.changespeed(0, -3)
                contextObject.player.image = tank_up
                
            elif event.key == pygame.K_s:
                contextObject.player.changespeed(0, 3)
                contextObject.player.image = tank_down        


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                contextObject.player.changespeed(3, 0)
                Dispatcher.dispatch()
                
            elif event.key == pygame.K_d:
                contextObject.player.changespeed(-3, 0)
                Dispatcher.dispatch()
                
            elif event.key == pygame.K_w:
                contextObject.player.changespeed(0, 3)
                Dispatcher.dispatch()
                
            elif event.key == pygame.K_s:
                contextObject.player.changespeed(0, -3)
                Dispatcher.dispatch()
                
        if pygame.key.get_pressed()[pygame.K_q]:
            quit()
 
    all_sprite_list.update() 
    
    background = pygame.image.load("Images/grass.png")
    contextObject.screen.blit(background, (0, 0))
 
    all_sprite_list.draw(contextObject.screen)
 
    pygame.display.flip()
 
    clock.tick(60)
    

pygame.quit()
