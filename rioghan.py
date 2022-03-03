import sys, pygame

pygame.init()

window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

pygame.display.set_caption('Tank Trouble')

tank = pygame.image.load('Images/tank.png')

background = pygame.image.load("Images/grass.png")

background = pygame.transform.scale(background, (1920, 1080))

height = window.get_height()/10
width = window.get_width()/10

tank = pygame.transform.scale(tank, (width, height))

tank_up = pygame.transform.rotate(tank, 0)

tank_left = pygame.transform.rotate(tank, 90)

tank_down = pygame.transform.rotate(tank, 180)

tank_right = pygame.transform.rotate(tank, 270)


class Player(object):
    
    def __init__(self):
        self = window.blit(tank, (x, y))
 
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

x = 100
y = 100

velocity = 2

walls = [] # List to hold the walls
tank1 = Player()


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


run = True
while run:

	for event in pygame.event.get():

		if event.type == pygame.VIDEORESIZE:
			# There's some code to add back window content here.
			surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()

		if pygame.key.get_pressed()[pygame.K_a]:
			x -= velocity
			y = y + 0
			tank = tank_left

		elif pygame.key.get_pressed()[pygame.K_d]:
			x += velocity
			y = y + 0
			tank = tank_right

		elif pygame.key.get_pressed()[pygame.K_w]:
			y -= velocity
			x = x + 0
			tank = tank_up

		elif pygame.key.get_pressed()[pygame.K_s]:
			y += velocity
			x = x + 0
			tank = tank_down

		if pygame.key.get_pressed()[pygame.K_q]:
			quit()
			
            
		# From here we will draw the scene
		window.blit(background, (0, 0))
		window.blit(tank, (x, y))

		for wall in walls:
			pygame.draw.rect(window, (255, 255, 255), wall.rect)# Determine the wall
			

		pygame.display.flip()

		

		pygame.display.update()
