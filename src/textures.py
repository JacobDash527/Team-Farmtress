import pygame
import ui_classes

bread_monster = pygame.transform.scale(pygame.image.load("images/bread_monster.png"), (100, 100))
bg = pygame.image.load("images/bg.png").convert_alpha()
arrow_sheet = ui_classes.SpriteSheet(pygame.image.load("sprite_sheets/arrow_sheet.png"))
teleporter = pygame.transform.scale(pygame.image.load("images/teleporter.png"), (120, 100))