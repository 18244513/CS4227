import os
import sys
import random
import pygame
import numpy as np

from collections import deque

level = np.full((45, 60), 0)  # creates the dimenstions of matrix
rows = len(level)             # Gets rows in matrix
cols = len(level[0])          # Gets cols in matrix

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

# from here the this class will hold a wall rect
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.walls = None

# from here we store the matrix coords to use to clear the maze from unusable spaces
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

# this will store a data structurew for the queues used later in the code
class queueNode:
	def __init__(self,pt: Point, dist: int):
		self.pt = pt
		self.dist = dist

#From here e can check and see if a cell is valid
def isValid(ROW: int, COL: int):
    return (ROW >= 0) and (ROW < rows) and (COL >= 0) and (COL < cols)

#here we can get the north, south, east and west of the row and colum nodes in the matrix
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


def Path(level, p: Point, end: Point):
	
	# from here this will check to see if the matrix has a value of 1 and the start(p) or end(end)
	if level[p.x][p.y]!=1 or level[end.x][end.y]!=1:
		return -1
	
	visited = [[False for i in range(cols)]
					for j in range(rows)]
	
	# this wil Mark the starting cell as visited
	visited[p.x][p.y] = True
	
	# Create a queue for Path
	q = deque()
	
	# Distance of starting cell is 0
	s = queueNode(p,0)
	q.append(s)
	
	# Do a Path starting from source cell
	while q:

		curr = q.popleft() # Dequeue the front cell
		
		# If we have reached the end cell this will end
		pt = curr.pt
		if pt.x == end.x and pt.y == end.y:
			return curr.dist
		
		for i in range(4):
			ROW = pt.x + rowNum[i]
			COL = pt.y + colNum[i]
			
			# from here it will check other nodes not visited to try and find a path
			if (isValid(ROW,COL) and
			level[ROW][COL] == 1 and
				not visited[ROW][COL]):
				visited[ROW][COL] = True
				Adjcell = queueNode(Point(ROW,COL),
									curr.dist+1)
				q.append(Adjcell)
	
	# Return -1 if destination cannot be reached
	return -1



# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# here we set up the display
screen = pygame.display.set_mode((960, 720))
 
walls = [] # List to hold the walls
player = Player()

class Maze():

    #Here the maze is created using a 2D array
    #This can later be modified to give a random 2D array with
    #random variables
    i = 0
    j = 0

    while i < rows:
        level[i][0] = 1
        level[i][cols - 1] = 1

        i += 1

    while j < cols:
        level[0][j] = 1
        level[rows - 1][j] = 1
        j += 1

    #here I create empty space beside the barriers of the maze
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            node = random.randint(0, 1)
            level[i][j] = node
            j = j + 1
        i = i + 1
        

    for n in range(1, 2):
    #Here I find any spaces that are reachable and unreachable
        start = Point(2,2)
        for i in range(2, rows-1):
            for j in range(2, cols - 1):
                if(level[i][j] == 1):
                    j = j + 1
                else:
                    #for those spaces I run the Path def to create space next to each unreachable path 
                    end = Point(i,j)
                    dist = Path(level,start,end)
                    number = random.randint(0, 1)
                    if (dist==-1 and number == 0):
                        level[i][j] = 0
                        j = j - 1
                    if (dist==-1 and number == 0):
                        level[i][j] = 0
                        j = j - 1
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
        # Determine the wall what the wall looks like
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        #creates a test player that can interact with the wall
        pygame.draw.rect(screen, (255, 0, 0), player.rect)
    pygame.display.flip()
 
pygame.quit()