# Cathal Kelly 18244513

import pygame
from pdb import main
import sys
from atexit import register
from sre_constants import IN
from tank import Tank
from Invoker import Invoker
from MoveCommand import MoveUpCommand
from MoveCommand import MoveDownCommand
from MoveCommand import MoveRightCommand
from MoveCommand import MoveLeftCommand
from ShootCommand import ShootCommand

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
pygame.init()
pygame.display.set_caption('Tank Trouble')
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
all_sprite_list = pygame.sprite.Group()

clock = pygame.time.Clock()

TANK = Tank(50, 50)
all_sprite_list.add(TANK)

MOVE_UP = MoveUpCommand(TANK)
MOVE_DOWN = MoveDownCommand(TANK)
MOVE_RIGHT = MoveRightCommand(TANK)
MOVE_LEFT = MoveLeftCommand(TANK)
SHOOT = ShootCommand(TANK)

INVOKER = Invoker()
INVOKER.register("UP", MOVE_UP)
INVOKER.register("DOWN", MOVE_DOWN)
INVOKER.register("RIGHT", MOVE_RIGHT)
INVOKER.register("LEFT", MOVE_LEFT)
INVOKER.register("SHOOT", SHOOT)

tank_up = pygame.transform.rotate(TANK.image, 0)
tank_left = pygame.transform.rotate(TANK.image, 90)
tank_down = pygame.transform.rotate(TANK.image, 180)
tank_right = pygame.transform.rotate(TANK.image, 270)

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
                TANK.image = tank_left

            elif pygame.key.get_pressed()[pygame.K_d]:
                INVOKER.execute("RIGHT")
                TANK.image = tank_right

            elif pygame.key.get_pressed()[pygame.K_w]:
                INVOKER.execute("UP")
                TANK.image = tank_up

            elif pygame.key.get_pressed()[pygame.K_s]:
                INVOKER.execute("DOWN")
                TANK.image = tank_down
                
            elif pygame.key.get_pressed()[pygame.K_e]:
                INVOKER.execute("SHOOT")

    all_sprite_list.update() 

    background = pygame.image.load("Images/grass.png")
    screen.blit(background, (0, 0))

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()