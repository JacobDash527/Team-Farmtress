import pygame
import ui_classes


bread_monster = pygame.transform.scale(pygame.image.load("src/images/bread_monster.png"), (100, 100))

bg = pygame.transform.scale(pygame.image.load("src/images/bg.png").convert_alpha(), (1800, 1200))
arrow_sheet = ui_classes.SpriteSheet(pygame.image.load("src/sprite_sheets/arrow_sheet.png"))
teleporter = pygame.transform.scale(pygame.image.load("src/images/teleporter.png"), (120, 100))
plant_menu = pygame.image.load("src/images/plantmenu.png").convert_alpha()
breads_menu = pygame.transform.scale(pygame.image.load("src/images/breads_menu.png"), (pygame.image.load("src/images/breads_menu.png").get_width() * 2, pygame.image.load("src/images/breads_menu.png").get_height() * 2))
cash_money = pygame.image.load("src/images/cash_money.png")

harvester = pygame.image.load("src/images/harvester.png")
plant = pygame.image.load("src/images/plant.png")
watering_can = pygame.image.load("src/images/watering_can.png")
tool_outline = pygame.transform.scale(pygame.image.load("src/images/border.png"), (pygame.image.load("src/images/border.png").get_width() * 0.7, pygame.image.load("src/images/border.png").get_height() * 0.7))