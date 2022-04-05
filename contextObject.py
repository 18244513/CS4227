# Rioghan Lowry 18226531

import pygame
from player import Player

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
player = Player(50, 50)

class contextObject ():
    def getXCoords():
        x_coords = 'x = ' + str(player.rect.x)
        print(x_coords)
    
    def getYCoords():
        y_coords = 'y = ' + str(player.rect.y)
        print(y_coords)