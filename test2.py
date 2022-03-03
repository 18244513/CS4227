from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('Images/tank.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

'''
Setup
'''

backdrop = pygame.image.load(os.path.join('Images/grass.png'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

'''
Rotate tank 
'''
tank_up = pygame.transform.rotate(player.image, 0)
tank_left = pygame.transform.rotate(player.image, 90)
tank_down = pygame.transform.rotate(player.image, 180)
tank_right = pygame.transform.rotate(player.image, 270)


'''
Main Loop
'''
velocity = 12

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if pygame.key.get_pressed()[pygame.K_a]:
            player.rect.x -= velocity
            player.rect.y = player.rect.y + 0
            player.image = tank_left

        elif pygame.key.get_pressed()[pygame.K_d]:
            player.rect.x += velocity
            player.rect.y = player.rect.y + 0
            player.image = tank_right

        elif pygame.key.get_pressed()[pygame.K_w]:
            player.rect.y -= velocity
            player.rect.x = player.rect.x + 0
            player.image = tank_up

        elif pygame.key.get_pressed()[pygame.K_s]:
            player.rect.y += velocity
            player.rect.x = player.rect.x + 0
            player.image = tank_down

        if pygame.key.get_pressed()[pygame.K_q]:
            quit()

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)