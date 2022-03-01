import os
import sys
import random
import pygame
import numpy as np

# from here the this class will hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.walls = None

 
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# here we set up the display
screen = pygame.display.set_mode((400, 400))
 
walls = [] # List to hold the walls

class Maze():

    #Here the maze is created using a 2D array
    #This can later be modified to give a random 2D array with
    #random variables
    level = np.full((11, 11), 0)  # random values

    i = 0
    j = 0

    rows = len(level)

    cols = len(level[0])

    

    print(cols)

    while i < rows:
        level[i][0] = 1
        level[0][i] = 1
        level[i][cols - 1] = 1
        level[rows - 1][i] = 1

        i += 1
        if i == rows:
            break

        print(level)


        x = y = 0
        for row in level:
            for col in row:
                if col == 1:
                    Wall((x, y))
                x += 16
            y += 16
            x = 0


running = True
while running:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

 
 
    # Feom here we will draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)# Determine the wall what the wall looks like
    pygame.display.flip()
 
pygame.quit()