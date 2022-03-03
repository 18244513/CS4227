import pygame
WHITE = (255, 255, 255)
 
class Tank(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        self.image = pygame.image.load("Images/tank.png").convert_alpha()
        
    # THE MAIN ROTATE FUNCTION
    def rot(self):
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)
