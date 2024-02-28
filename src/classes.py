import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def colliding(self, pos):
        x, y = pos
        if self.x < x < (self.x + self.image.get_width()) and self.y < y < (self.y + self.image.get_height()):
            return True
        else:
            pass

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return(image)