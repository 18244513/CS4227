import sys, pygame



from PIL import Image

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    resized_image.save(output_image_path)

if __name__ == '__main__':
    resize_image(input_image_path='tank.jpg',
                 output_image_path='tank2.png',
                 size=(100, 100))

pygame.init()

window = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption('Tank Trouble')

tank = pygame.image.load('tank2.png')

background = pygame.image.load("grass2.png")

x = 100
y = 100

velocity = 12

run = True
while run:

	window.blit(background, (0, 0))

	window.blit(tank, (x, y))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()


		if event.type == pygame.KEYDOWN:

			if event.key == ord('a'):
				x -= velocity

			if event.key == ord('d'):
				x += velocity

			if event.key == ord('w'):
				y -= velocity

			if event.key == ord('s'):
				y += velocity

			if event.key == ord('q'):
				quit()

		pygame.display.update()
