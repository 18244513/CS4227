from typing import Tuple

import pygame
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

class GameState():
    def __init__(self):
        self.x = 120
        self.y = 120
        
    def update(self, moveCommandX, moveCommandY):
        self.x += moveCommandX
        self.y += moveCommandY

class Command():
    def __init__(self, value):
        self.value = value
        
    def incValue(self):
        self.value += 1
        
Command = Command(10)
print(Command.value)
Command.incValue()
print(Command.value)
    
class UserInterface():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Tank Trouble Command Pattern")
        self.clock = pygame.time.Clock()
        self.gameState = GameState()
        self.running = True
        self.moveCommandX = 0
        self.moveCommandY = 0
    def processInput(self):
        self.moveCommandX = 0
        self.moveCommandY = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif pygame.key.get_pressed()[pygame.K_q]:
                self.running = False
                break
            elif pygame.key.get_pressed()[pygame.K_d]:
                self.moveCommandX += 8
            elif pygame.key.get_pressed()[pygame.K_a]:
                self.moveCommandX -= 8
            elif pygame.key.get_pressed()[pygame.K_s]:
                self.moveCommandY += 8
            elif pygame.key.get_pressed()[pygame.K_w]:
                self.moveCommandY -= 8
    def update(self):
        self.gameState.update(self.moveCommandX, self.moveCommandY)
    def render(self):
        self.window.fill((0,0,0))
        x = self.gameState.x
        y = self.gameState.y
        pygame.draw.rect(self.window,(0,0,255),(x,y,400,240))
        pygame.display.update()
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()        
            self.clock.tick(60)
            
userInterface = UserInterface()
userInterface.run()


# '''
# Variables
# '''

# worldx = 960
# worldy = 720
# fps = 40
# ani = 4
# world = pygame.display.set_mode([worldx, worldy])

# BLUE = (25, 25, 200)
# BLACK = (23, 23, 23)
# WHITE = (254, 254, 254)
# ALPHA = (0, 255, 0)

# '''
# Objects
# '''


# class Player(pygame.sprite.Sprite):
#     """
#     Spawn a player
#     """

#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.movex = 0
#         self.movey = 0
#         self.frame = 0
#         self.images = []
#         for i in range(1, 5):
#             img = pygame.image.load(os.path.join('images', 'tank' + str(i) + '.png')).convert()
#             img.convert_alpha()  # optimise alpha
#             img.set_colorkey(ALPHA)  # set alpha
#             self.images.append(img)
#             self.image = self.images[0]
#             self.rect = self.image.get_rect()

#     def control(self, x, y):
#         """
#         control player movement
#         """
#         self.movex += x
#         self.movey += y

#     def update(self):
#         """
#         Update sprite position
#         """

#         self.rect.x = self.rect.x + self.movex
#         self.rect.y = self.rect.y + self.movey

#         # moving left
#         if self.movex < 0:
#             self.frame += 1
#             if self.frame > 3*ani:
#                 self.frame = 0
#             self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

#         # moving right
#         if self.movex > 0:
#             self.frame += 1
#             if self.frame > 3*ani:
#                 self.frame = 0
#             self.image = self.images[self.frame//ani]


# '''
# Setup
# '''

# backdrop = pygame.image.load(os.path.join('images', 'grass.png'))
# clock = pygame.time.Clock()
# pygame.init()
# backdropbox = world.get_rect()
# main = True

# player = Player()  # spawn player
# player.rect.x = 0  # go to x
# player.rect.y = 0  # go to y
# player_list = pygame.sprite.Group()
# player_list.add(player)

# '''
# Main Loop
# '''
# velocity = 12

# while main:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             try:
#                 sys.exit()
#             finally:
#                 main = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == ord('q'):
#                 pygame.quit()
#                 try:
#                     sys.exit()
#                 finally:
#                     main = False
#         if pygame.key.get_pressed()[pygame.K_a]:
#             player.rect.x -= velocity
#             player.rect.y = player.rect.y + 0

#         elif pygame.key.get_pressed()[pygame.K_d]:
#             player.rect.x += velocity
#             player.rect.y = player.rect.y + 0

#         elif pygame.key.get_pressed()[pygame.K_w]:
#             player.rect.y -= velocity
#             player.rect.x = player.rect.x + 0

#         elif pygame.key.get_pressed()[pygame.K_s]:
#             player.rect.y += velocity
#             player.rect.x = player.rect.x + 0

#     world.blit(backdrop, backdropbox)
#     player.update()
#     player_list.draw(world)
#     pygame.display.flip()
#     clock.tick(fps)
    
    
# from abc import ABC, abstractmethod
# class Command(ABC):
#     def __init__(self, receiver):
#         self.receiver = receiver
        
#     def process(self):
#         pass
    
# class CommandImplementation(Command):
#     def __init__(self, receiver):
#         self.receiver = receiver
        
#     def process(self):
#         self.receiver.perform_action()
        
# class Receiver:
#     def perform_action(self):
#         print('Action performed in receiver.')
        
# class Invoker:
#     def command(self, cmd):
#         self.cmd = cmd
        
#     def execute(self):
#         self.cmd.process()
        