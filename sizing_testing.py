from tkinter import Image


image = Image.open('grass.png')
new_image = image.resize((960, 720))
new_image.save('resized_grass.png')

print(image.size) # Output: (1920, 1280)
print(new_image.size) # Output: (400, 400)