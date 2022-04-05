# Rioghan Lowry 18226531

from pdb import main
import sys
import pygame
import contextObject
from wall import Wall
from dispatcher import Dispatcher


'''
cathal
'''
from atexit import register
from sre_constants import IN
from tank import Tank
from Invoker import Invoker
from MoveCommand import MoveUpCommand
from MoveCommand import MoveDownCommand
from MoveCommand import MoveRightCommand
from MoveCommand import MoveLeftCommand
from ShootCommand import ShootCommand
 
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
cathal move 
'''
MOVE_UP = MoveUpCommand(contextObject.player)
MOVE_DOWN = MoveDownCommand(contextObject.player)
MOVE_RIGHT = MoveRightCommand(contextObject.player)
MOVE_LEFT = MoveLeftCommand(contextObject.player)
SHOOT = ShootCommand(contextObject.player)

INVOKER = Invoker()
INVOKER.register("UP", MOVE_UP)
INVOKER.register("DOWN", MOVE_DOWN)
INVOKER.register("RIGHT", MOVE_RIGHT)
INVOKER.register("LEFT", MOVE_LEFT)
INVOKER.register("SHOOT", SHOOT)
 
'''
Rotate tank 
'''
tank_up = pygame.transform.rotate(contextObject.player.image, 0)
tank_left = pygame.transform.rotate(contextObject.player.image, 90)
tank_down = pygame.transform.rotate(contextObject.player.image, 180)
tank_right = pygame.transform.rotate(contextObject.player.image, 270)     


'''
Cathal
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if pygame.key.get_pressed()[pygame.K_a]:
                INVOKER.execute("LEFT")
                contextObject.player.image = tank_left
                Dispatcher.dispatch()

            elif pygame.key.get_pressed()[pygame.K_d]:
                INVOKER.execute("RIGHT")
                contextObject.player.image = tank_right
                Dispatcher.dispatch()

            elif pygame.key.get_pressed()[pygame.K_w]:
                INVOKER.execute("UP")
                contextObject.player.image = tank_up
                Dispatcher.dispatch()

            elif pygame.key.get_pressed()[pygame.K_s]:
                INVOKER.execute("DOWN")
                contextObject.player.image = tank_down
                Dispatcher.dispatch()
                
            elif pygame.key.get_pressed()[pygame.K_e]:
                INVOKER.execute("SHOOT")
 
    all_sprite_list.update() 
    
    background = pygame.image.load("Images/grass.png")
    contextObject.screen.blit(background, (0, 0))
 
    all_sprite_list.draw(contextObject.screen)
 
    pygame.display.flip()
 
    clock.tick(60)
    

pygame.quit()
