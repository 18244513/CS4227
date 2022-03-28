import numpy as np
import random
import pygame

walls = []

#Here the class Director controls the construction process of the Game
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getMaze(self):
        game = Game()

        matrix = self.__builder.getMatrix()
        game.setMatrix(matrix)

        wall = self.__builder.getWalls()
        game.setWalls(wall)

        player = self.__builder.getPlayer()
        game.setPlayer(player)

        return game

#here is the final product that will be used by the director and use the parts in Builder the 
class Game:
    def __init__(self):
        self.__matrix = None

    def setMatrix(self, matrix):
        self.__matrix = matrix

    def setWalls(self, wall):
        self.__wall = wall

    def setPlayer(self, player):
        self.__player = player


#here we have the seperate parts of the Game that will be used by the Concrete Builder
class Builder:
    def getMatrix(self):
        pass

    def getWall(self): 
        pass

    def getPlayer(self): 
        pass



#here is the concrete builder for creating a maze that is random
class RandMaze(Builder):

    def __init__(self):
        self.matrix = np.full((45, 60), 0)
        self.rect = pygame.Rect(32, 32, 16, 16)
        self.screen = pygame.display.set_mode((960, 720))
        self.running = True

    def getMatrix(self):

        matrix = self.matrix

        rows = len(matrix)             # Gets rows in matrix
        cols = len(matrix[0])          # Gets cols in matrix

        #Sets the outsides of the matrix to 1
        for i in range(0, rows):
            matrix[i][0] = 1
            matrix[i][cols - 1] = 1
            i += 1

        #Sets the 1 from the outsides of the matrix to 0
        for j in range(0, cols):
            matrix[0][j] = 1
            matrix[rows - 1][j] = 1
            j += 1

        #Randomize the center of the maze from 0's and 1's
        for i in range(2, rows - 2):
            for j in range(2, cols - 2):
                node = random.randint(0, 1)
                matrix[i][j] = node
                j = j + 1
            i = i + 1        


    def getWalls(self):

        #Places walls where 1 is in the matrix
        matrix = self.matrix
        x = y = 0
        for row in matrix:
            for col in row:
                if col == 1:
                    Walls((x, y))
                x += 16
            y += 16
            x = 0

        return matrix



    def getPlayer(self):

        player = Player()
        
        screen = self.screen
        self.running = True

        #While the game runs the player can move with the arrow keys and closed by the ESC button
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







#here is the concrete builder for creating a maze that has + instead of being random
class NonRandMaze(Builder):

    def __init__(self):
        self.matrix = np.full((43, 60), 0)
        self.rect = pygame.Rect(32, 32, 16, 16)
        self.walls = np.array

    def getMatrix(self):

        matrix = self.matrix

        rows = len(matrix)             # Gets rows in matrix
        cols = len(matrix[0])          # Gets cols in matrix

        for i in range(0, rows):
            matrix[i][0] = 1
            matrix[i][cols - 1] = 1
            i += 1

        for j in range(0, cols):
            matrix[0][j] = 1
            matrix[rows - 1][j] = 1
            j += 1


        #Rather than 
        for i in range(3, rows - 2, 4):
            for j in range(3, cols - 2, 4):
                node = 1
                matrix[i][j] = node
                matrix[i - 1][j] = node
                matrix[i + 1][j] = node
                matrix[i][j - 1] = node
                matrix[i][j + 1] = node


    def getWalls(self):

        matrix = self.matrix
        x = y = 0
        for row in matrix:
            for col in row:
                if col == 1:
                    Walls((x, y))
                x += 16
            y += 16
            x = 0

        return matrix

        


    def getPlayer(self):

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
            screen.fill((0, 0, 255))
            for wall in walls:
                # Determine the wall what the wall looks like
                pygame.draw.rect(screen, (0, 255, 0), wall.rect)
                #creates a test player that can interact with the wall
                pygame.draw.rect(screen, (255, 0, 0), player.rect)
            pygame.display.flip()






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






def main():
    randMaze = True

    if randMaze == True:
        Maze = RandMaze()
    else:
        Maze = NonRandMaze()

    director = Director()
    director.setBuilder(Maze)
    maze = director.getMaze()
    print(maze)


main()