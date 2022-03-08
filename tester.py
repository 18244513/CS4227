import os
import sys
import random
import pygame
import numpy as np


class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
 
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# from here the this class will hold a wall rect
class Walls(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.walls = None

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
 
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
 
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# here we set up the display
screen = pygame.display.set_mode((400, 400))
 
walls = [] # List to hold the walls
player = Player()


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
         [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],   #10
         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],   #11
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


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

 
 
    # Feom here we will draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)# Determine the wall
        pygame.draw.rect(screen, (255, 0, 0), player.rect)
    pygame.display.flip()
 
pygame.quit()