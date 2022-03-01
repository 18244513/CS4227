import sys, pygame

pygame.init()

window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

pygame.display.set_caption('Tank Trouble')

tank = pygame.image.load('Images/tank.png')



height = window.get_height()/10
width = window.get_width()/10

tank = pygame.transform.scale(tank, (width, height))



background = pygame.image.load("Images/grass.png")

background = pygame.transform.scale(background, (1920, 1080))

tank_up = pygame.transform.rotate(tank, 0)

tank_left = pygame.transform.rotate(tank, 90)

tank_down = pygame.transform.rotate(tank, 180)

tank_right = pygame.transform.rotate(tank, 270)



x = 100
y = 100

velocity = 2

run = True
while run:

	window.blit(background, (0, 0))

	window.blit(tank, (x, y))

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

		pygame.display.update()

