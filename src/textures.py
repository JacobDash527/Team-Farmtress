import pygame
import ui_classes

bread_monster = pygame.transform.scale(pygame.image.load("images/bread_monster.png"), (100, 100))
bg = pygame.image.load("images/bg.png").convert_alpha()
arrow_sheet = ui_classes.SpriteSheet(pygame.image.load("sprite_sheets/arrow_sheet.png"))
teleporter = pygame.transform.scale(pygame.image.load("images/teleporter.png"), (120, 100))
plant_menu = pygame.image.load("images/plantmenu.png").convert_alpha()
breads_menu = pygame.transform.scale(pygame.image.load("images/breads_menu.png"), (pygame.image.load("images/breads_menu.png").get_width() * 2, pygame.image.load("images/breads_menu.png").get_height() * 2))