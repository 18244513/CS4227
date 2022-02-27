#! /usr/bin/env python
 
import os
import sys
import random
import pygame
import numpy as np

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
 
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
screen = pygame.display.set_mode((400, 400))
 
walls = [] # List to hold the walls


#Here the maze is created using a 2D array
#This can later be modified to give a random 2D array with
#random variables
level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   #1
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   #2
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],   #3
         [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],   #4
         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],   #5
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],   #6
         [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],   #7
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],   #8
         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],   #9
         [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],   #10
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],   #11
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],   #12
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]   #13


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

 
 
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.display.flip()
 
pygame.quit()