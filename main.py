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
            img = pygame.image.load(os.path.join('images', 'tank' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
        
        # enemy_hit_list = pygame.sprite.spritecollide(self, enemy.rect, False)
        # for enemy in enemy_hit_list:
        #     if self.change_x > 0:
        #         self.rect.right = enemy.rect.left
        #     else:
        #         self.rect.left = enemy.rect.right
                
        # self.rect.y += self.change_y
        
        # enemy_hit_list = pygame.sprite.spritecollide(self, enemy.rect, False)
        # for enemy in enemy_hit_list:

        #     if self.change_y > 0:
        #         self.rect.bottom = enemy.rect.top
        #     else:
        #         self.rect.top = enemy.rect.bottom
                        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if x < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if y > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if y < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
            
        
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images',img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        
    def move(self):
        distance = 80
        speed = 8
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
        
        self.counter += 1
        
        # player_hit_list = pygame.sprite.spritecollide(self, player.rect, False)
        # for player in player_hit_list:
        #     if self.change_x > 0:
        #         self.rect.right = player.rect.left
        #     else:
        #         self.rect.left = player.rect.right
                
        # self.rect.y += self.change_y
        
        # player_hit_list = pygame.sprite.spritecollide(self, player.rect, False)
        # for player in player_hit_list:

        #     if self.change_y > 0:
        #         self.rect.bottom = enemy.rect.top
        #     else:
        #         self.rect.top = enemy.rect.bottom

class Walls(pygame.sprite.Sprite):
    
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

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
 

'''
Setup
'''

backdrop = pygame.image.load(os.path.join('images', 'grass.png'))
backdrop = pygame.transform.scale(backdrop, (1280, 720))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True
walls = []

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10

enemy = Enemy(300,0,'enemy.png')
enemy.rect.x = 100
enemy.rect.y = 100
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
# eloc = []
# eloc = [300, 0]

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

'''
Main Loop
'''
velocity = 12

tank_up = pygame.transform.rotate(player.image, 0)
tank_left = pygame.transform.rotate(player.image, 90)
tank_down = pygame.transform.rotate(player.image, 180)
tank_right = pygame.transform.rotate(player.image, 270)

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
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

    xchange = (enemy.rect.x - player.rect.x)/100
    ychange = (enemy.rect.y - player.rect.y)/100
    enemy.rect.x -= xchange
    enemy.rect.y -= ychange

    world.blit(backdrop, backdropbox)
    for wall in walls:
        pygame.draw.rect(world, (255, 255, 255), wall.rect)# Determine the wall
        pygame.draw.rect(world, (255, 0, 0), player.rect)
        pygame.draw.rect(world, (0, 255, 0), enemy.rect)
    pygame.display.flip()
    player.update()
    player_list.draw(world)
    enemy_list.draw(world)
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)
        