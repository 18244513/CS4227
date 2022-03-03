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
screen = pygame.display.set_mode((960, 720))
 
walls = [] # List to hold the walls

class Maze():

    #Here the maze is created using a 2D array
    #This can later be modified to give a random 2D array with
    #random variables


    level = np.full((45, 60), 0)  # random values

    i = 0
    j = 0

    rows = len(level)

    cols = len(level[0])

    while i < rows:
        level[i][0] = 1
        level[i][cols - 1] = 1

        i += 1

    while j < cols:
        level[0][j] = 1
        level[rows - 1][j] = 1
        j += 1




    

    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            node = random.randint(0, 1)
            level[i][j] = node
            j = j + 1
        i = i + 1
        

    x = y = 0
    for row in level:
        for col in row:
            if col == 1:
                Wall((x, y))
            x += 16
        y += 16
        x = 0



    def isPath(level):
        rows = 10
        cols = 15
        for i in range(1, rows):
            if (level[i][0] != 1):
                level[i][0] = level[i-1][0]

        for j in range(1, cols):
            if (level[0][j] != 1):
                level[0][j] = level[0][j-1]

        return (level[rows - 1][cols - 1] == 1)



    print(level)

    if (isPath(level)):
        print("Yes")
    else:
	    print("No")


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