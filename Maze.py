import numpy as np
import random
import pygame

walls = []

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getMaze(self):
        game = Game()

        maze = self.__builder.getMazeWalls()
        game.setMazeWalls(maze)

        wall = self.__builder.getWalls()
        game.setWalls(wall)

        display = self.__builder.getDisplay()
        game.setDisplay(display)


        return game

        

class Game:
    def __init__(self):
        self.__maze = None


    def setMazeWalls(self, maze):
        self.__maze = maze

    def setWalls(self, wall):
        self.__wall = wall

    def setDisplay(self, display):
        self.__display = display

    def specification(self):
        print(self.__maze)
        print(self.__display)




class Builder:
    def getMazeWalls(self): pass
    def getWall(self): pass
    def getPath(self): pass
    def getDisplay(self): pass




class RandMaze(Builder):

    def __init__(self):
        self.maze = np.full((45, 60), 0)
        self.rect = pygame.Rect(32, 32, 16, 16)
        self.screen = pygame.display.set_mode((960, 720))
        self.running = True

    def getMazeWalls(self):

        maze = self.maze

        rows = len(maze)             # Gets rows in matrix
        cols = len(maze[0])          # Gets cols in matrix

    
        i = 0
        j = 0

        for i in range(0, rows):
            maze[i][0] = 1
            maze[i][cols - 1] = 1
            i += 1

        for i in range(0, cols):
            maze[0][j] = 1
            maze[rows - 1][j] = 1
            j += 1

        for i in range(2, rows - 2):
            for j in range(2, cols - 2):
                node = random.randint(0, 1)
                maze[i][j] = node
                j = j + 1
            i = i + 1        


    def getWalls(self):

        maze = self.maze
        x = y = 0
        for row in maze:
            for col in row:
                if col == 1:
                    Walls((x, y))
                x += 16
            y += 16
            x = 0

        return maze



    def getDisplay(self):

        player = Player()
        
        screen = self.screen
        self.running = True

        while self.running:
    
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
                
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
                # Determine the wall what the wall looks like
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
                #creates a test player that can interact with the wall
                pygame.draw.rect(screen, (255, 0, 0), player.rect)
            pygame.display.flip()



class NonRandMaze(Builder):

    def __init__(self):
        self.maze = np.full((43, 60), 0)
        self.rect = pygame.Rect(32, 32, 16, 16)
        self.walls = np.array

    def getMazeWalls(self):

        maze = self.maze

        rows = len(maze)             # Gets rows in matrix
        cols = len(maze[0])          # Gets cols in matrix

    

        for i in range(0, rows):
            maze[i][0] = 1
            maze[i][cols - 1] = 1
            i += 1

        for j in range(0, cols):
            maze[0][j] = 1
            maze[rows - 1][j] = 1
            j += 1



        for i in range(3, rows - 2, 4):
            for j in range(3, cols - 2, 4):
                node = 1
                maze[i][j] = node
                maze[i - 1][j] = node
                maze[i + 1][j] = node
                maze[i][j - 1] = node
                maze[i][j + 1] = node


    def getWalls(self):

        maze = self.maze
        x = y = 0
        for row in maze:
            for col in row:
                if col == 1:
                    Walls((x, y))
                x += 16
            y += 16
            x = 0

        return maze

        


    def getDisplay(self):

        player = Player()
        
        screen = pygame.display.set_mode((960, 690))
        self.running = True

        while self.running:
    
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
                
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
                # Determine the wall what the wall looks like
                pygame.draw.rect(screen, (255, 255, 255), wall.rect)
                #creates a test player that can interact with the wall
                pygame.draw.rect(screen, (255, 0, 0), player.rect)
            pygame.display.flip()
    


class Matrix:
   matrix = []

class Display:
    screen = pygame.display.set_mode((960, 720))

class Walls(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.walls = None


class Player(object):
    
    def __init__(self):
        #sets the position of the player
        self.rect = pygame.Rect(16, 16, 16, 16)
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the player
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

class Path():

    def __init__(self):
        cla = RandMaze()
        self.matrix = cla.getMazeWalls()


def main():
    rand = False

    if rand == True:
        Maze = RandMaze()
    else:
        Maze = NonRandMaze()

    director = Director()

    director.setBuilder(Maze)
    maze = director.getMaze()
    maze.specification()
    print(maze)


main()