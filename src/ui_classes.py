import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Button():
    def __init__(self, x, y, image, scale):
        self.clicked = False
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.enabled = True

    def draw(self, x, y, scale, greyscale):
        draw_image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        if greyscale:
            draw_image = pygame.transform.grayscale(draw_image)
        screen.blit(draw_image, (x, y))

    def is_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if self.enabled == True: 
                    return(True)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def colliding(self, pos):
        x, y = pos
        if self.x < x < (self.x + self.image.get_width()) and self.y < y < (self.y + self.image.get_height()):
            return True
        else:
            pass

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return(image)

class SideMenus():
    def __init__(self, closed, open):
        self.clicked = False
        self.open = False
        self.closed_sprite = pygame.transform.scale(closed, (closed.get_width() * 2, closed.get_height() * 2))
        self.open_sprite = pygame.transform.scale(open, (open.get_width() * 2, open.get_height() * 2))
        self.rect = self.closed_sprite.get_rect()
        self.rect.topleft = (548, 20)
        self.y = 20

    def draw(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if self.open == False:
                    self.open = True
                elif self.open == True:
                    self.open = False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if self.open == True:
            screen.blit(self.open_sprite, (548, self.y))
        elif self.open == False:
            screen.blit(self.closed_sprite, (548, self.y))