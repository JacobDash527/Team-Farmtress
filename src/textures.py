import pygame
import ui_classes

#privileged_bread = pygame.transform.scale(pygame.image.load("images/privileged_bread.png"), (100, 100))
privileged_bread = ["images/privileged_bread.png", 100, 100]
#bread_monster = pygame.transform.scale(pygame.image.load("images/bread_monster.png"), (100, 100))
bread_monster = ["images/bread_monster.png", 100, 100]
#bread_crab = pygame.transform.scale(pygame.image.load("images/bread_crab.png"), (100, 100))
bread_crab = ["images/bread_crab.png", 100, 100]
#baba_ganoush = pygame.transform.scale(pygame.image.load("images/baba_ganoush.png"), (100, 100))
baba_ganoush = ["images/baba_ganoush.png", 100, 100]

#bg = pygame.transform.scale(pygame.image.load("images/2fort.png").convert_alpha(), (1200, 900))
bg = ["images/2fort.png", 1200, 900]
arrow_sheet = ui_classes.SpriteSheet(pygame.image.load("sprite_sheets/arrow_sheet.png"))
#teleporter = pygame.transform.scale(pygame.image.load("images/teleporter.png"), (90, 75))
teleporter = ["images/teleporter.png", 90*1.4, 75*1.4]
#breads_menu = pygame.transform.scale(pygame.image.load("images/breads_menu.png"), (pygame.image.load("images/breads_menu.png").get_width() * 2.2, pygame.image.load("images/breads_menu.png").get_height() * 2.2))
breads_menu = ["images/breads_menu.png", 126*2.2, 200*2.2]
#inventory_menu = pygame.transform.scale(pygame.image.load("images/inventory_menu.png"), (pygame.image.load("images/inventory_menu.png").get_width() * 2.2, pygame.image.load("images/inventory_menu.png").get_height() * 2.2))
inventory_menu = ["images/inventory_menu.png", 126*2.2, 200*2.2]
#cash_money = pygame.image.load("images/cash_money.png")
cash_money = ["images/cash_money.png", 150, 60]
#menu_item_template = pygame.transform.scale(pygame.image.load("images/menu_item_template.png"), (pygame.image.load("images/menu_item_template.png").get_width() * 4.4, pygame.image.load("images/menu_item_template.png").get_height() * 4.4))
menu_item_template = ["images/menu_item_template.png", 119*2.2, 18*2.2]
#menu_outline = pygame.transform.scale(pygame.image.load("images/menu_outline.png"), (pygame.image.load("images/menu_outline.png").get_width() * 4.4, pygame.image.load("images/menu_outline.png").get_height() * 4.4))
menu_outline = ["images/menu_outline.png", 119*2.2, 18*2.2]
#save = pygame.transform.scale(pygame.image.load("images/save.png"), (60, 60))
save = ["images/save.png", 60, 60]
#clear_save = pygame.transform.scale(pygame.image.load("images/clear_save.png"), (60, 60))
clear_save = ["images/clear_save.png", 60, 60]

#harvester = pygame.image.load("images/harvester.png")
harvester = ["images/harvester.png", 100, 100]
#plant = pygame.image.load("images/plant.png")
plant = ["images/plant.png", 100, 100]
#watering_can = pygame.image.load("images/watering_can.png")
watering_can = ["images/watering_can.png", 100, 100]
#tool_outline = pygame.transform.scale(pygame.image.load("images/border.png"), (pygame.image.load("images/border.png").get_width() * 0.5, pygame.image.load("images/border.png").get_height() * 0.5))
tool_outline = ["images/border.png", 100, 100]

how_to_play = ["images/how_to_play.png", 1200, 900]
htp_button = ["images/htp_button.png", 60, 60]