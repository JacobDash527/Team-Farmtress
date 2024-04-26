import pygame
import ui_classes
import game_classes
import textures
import time
from SaveLoadManager import SaveLoadSystem
import pyvidplayer
import ffpyplayer

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

#[x, y, plant, plot_button, menu_open]
plots = []
plots.append([[0, 0, 'null', 'null', False], [0, 1, 'null', 'null', False], [0, 2, 'null', 'null', False], [0, 3, 'null', 'null', False], [0, 4, 'null', 'null', False]])
plots.append([[1, 0, 'null', 'null', False], [1, 1, 'null', 'null', False], [1, 2, 'null', 'null', False], [1, 3, 'null', 'null', False], [1, 4, 'null', 'null', False]])
plots.append([[2, 0, 'null', 'null', False], [2, 1, 'null', 'null', False], [2, 2, 'null', 'null', False], [2, 3, 'null', 'null', False], [2, 4, 'null', 'null', False]])
plots.append([[3, 0, 'null', 'null', False], [3, 1, 'null', 'null', False], [3, 2, 'null', 'null', False], [3, 3, 'null', 'null', False], [3, 4, 'null', 'null', False]])
plots.append([[4, 0, 'null', 'null', False], [4, 1, 'null', 'null', False], [4, 2, 'null', 'null', False], [4, 3, 'null', 'null', False], [4, 4, 'null', 'null', False]])

plots_default = []
plots_default.append([[0, 0, 'null', 'null', False], [0, 1, 'null', 'null', False], [0, 2, 'null', 'null', False], [0, 3, 'null', 'null', False], [0, 4, 'null', 'null', False]])
plots_default.append([[1, 0, 'null', 'null', False], [1, 1, 'null', 'null', False], [1, 2, 'null', 'null', False], [1, 3, 'null', 'null', False], [1, 4, 'null', 'null', False]])
plots_default.append([[2, 0, 'null', 'null', False], [2, 1, 'null', 'null', False], [2, 2, 'null', 'null', False], [2, 3, 'null', 'null', False], [2, 4, 'null', 'null', False]])
plots_default.append([[3, 0, 'null', 'null', False], [3, 1, 'null', 'null', False], [3, 2, 'null', 'null', False], [3, 3, 'null', 'null', False], [3, 4, 'null', 'null', False]])
plots_default.append([[4, 0, 'null', 'null', False], [4, 1, 'null', 'null', False], [4, 2, 'null', 'null', False], [4, 3, 'null', 'null', False], [4, 4, 'null', 'null', False]])

breads = ["Plain Bread: $5", "Bread Monster: $30", "Bread Crab: $10", "Baba Ganoush: $500"]
inventory = {"money":20, "plain_bread":4, "bread_monster":3, "bread_crab":0, "baba_ganoush": 100}
inventory_default = {"money":0, "plain_bread":1, "bread_monster":0, "bread_crab":0, "baba_ganoush": 0}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Team Farmtress')
arrow_frame_list = []
frame = 0
text_font = pygame.font.SysFont("Arial", 45)
side_menu_font = pygame.font.SysFont("Arial", 20)
stats = ""

selected_seed = 'plain_bread'
breads_menu_items = [ui_classes.Button(938, 47, textures.menu_item_template, 0.5), ui_classes.Button(938, 96, textures.menu_item_template, 0.5), ui_classes.Button(938, 145, textures.menu_item_template, 0.5), ui_classes.Button(938, 194, textures.menu_item_template, 0.5)]
inventory_menu_items = [ui_classes.Button(940, 492, textures.menu_item_template, 0.5), ui_classes.Button(940, 541, textures.menu_item_template, 0.5), ui_classes.Button(940, 590, textures.menu_item_template, 0.5), ui_classes.Button(938, 639, textures.menu_item_template, 0.5)]
inventory_outline = ui_classes.Button(940, 492, textures.menu_outline, 0.5)

selected_tool = ''
toolbar = [ui_classes.Button(30, 800, textures.plant, 0.5), ui_classes.Button(150, 800, textures.harvester, 0.5), ui_classes.Button(270, 800, textures.watering_can, 0.5)]

save = ui_classes.Button(5, 5, textures.save, 1)
clear_save = ui_classes.Button(5, 75, textures.clear_save, 1)
htp_button = ui_classes.Button(5, 145, textures.htp_button, 1)

intro_vid = pyvidplayer.Video("Mr Pixtel.mp4")
intro_vid.set_size((1200, 700))

clock = pygame.time.Clock()

run = True

for xindex, row in enumerate(plots):
  for yindex, column in enumerate(row):
    column[3] = ui_classes.Button(xindex * 135 + 90, yindex * 135 + 90, ["images/teleporter.png", 90*1.4, 75*1.4], 1.4)
    if column[2] != 'null':
      column[3].enabled = False

#ik its repeated its last minute ok :(
for xindex, row in enumerate(plots_default):
  for yindex, column in enumerate(row):
    column[3] = ui_classes.Button(xindex * 135 + 90, yindex * 135 + 90, ["images/teleporter.png", 90*1.4, 75*1.4], 1.4)
    if column[2] != 'null':
      column[3].enabled = False

def intro():
  intro_playing = True

  while intro_playing == True:
    intro_vid.draw(screen, (0, 75))
    pygame.display.update()
    if intro_vid._frame_num == intro_vid.frame_count-1:
      intro_vid.close()
      pygame.display.update()
      time.sleep(1)
      intro_playing = False
    for event in pygame.event.get():
      if event == pygame.MOUSEBUTTONDOWN:
        intro_vid.close()
        pygame.display.update()
        intro_playing = False

saveloadmanage = SaveLoadSystem(".save", "save_data")

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def test_buyable(balance, value):
  output = False
  if balance - value < 0:
    output = False
  else:
    output = True
  return(output)

intro()

plots, inventory = saveloadmanage.load_game_data(["plots", "inventory"], [plots_default, inventory_default])

while run:
  destroy = False
  clock.tick(10)

  screen.blit(ui_classes.get_image(textures.bg), (0, 0))

  for xindex, row in enumerate(plots):
    for yindex, column in enumerate(row):
      column[3].draw(xindex * 135 + 90, yindex * 135 + 90, 1, False)
      if column[2] != "null":
        destroy = column[2].tick()
        column[3].enabled = False
        column[2].draw(xindex, yindex)
        if destroy == True:
          column[2] = 'null'

      #use tools
      if column[3].is_clicked():
        #plant tool
        if selected_tool == 'plant':
          if inventory[selected_seed] >= 1:
            if selected_seed == 'plain_bread':
              column[2] = game_classes.PlainBread(xindex, yindex)
            elif selected_seed == 'bread_monster':
              column[2] = game_classes.BreadMonster(xindex, yindex)
            elif selected_seed == 'bread_crab':
              column[2] = game_classes.BreadCrab(xindex, yindex)
            elif selected_seed == 'baba_ganoush':
              column[2] = game_classes.BabaGanoush(xindex, yindex)

            inventory[selected_seed] += -1

      if column[2] != "null":
        new_stats = column[2].get_stats()
        if column[2].button.colliding(pygame.mouse.get_pos()):
          draw_text(f'Stage: {new_stats[0]}', side_menu_font, (0, 0, 0), xindex * 135 + 90, yindex * 135 + 180)
          draw_text(f'Hydration: {new_stats[1]}', side_menu_font, (0, 0, 0), xindex * 135 + 90, yindex * 135 + 200)
        if column[2].button.is_clicked():
          #harvest tool
          if selected_tool == 'harvest':
            harvest_data = column[2].harvest()
            inventory['money'] += harvest_data[0]
            inventory[column[2].type] += harvest_data[1]
            if harvest_data[2]:
              column[2] = 'null'
            column[3].enabled = True
          elif selected_tool == 'water':
            column[2].water()

      if column[3].colliding(pygame.mouse.get_pos()):
        screen.blit(textures.arrow_sheet.get_image(frame, 15, 50, 6, (0, 0, 0)), (column[3].x+18, column[3].y-150))

  draw_text(f"${inventory['money']}", text_font, (0, 0, 0), 170, 15)

  #select tools
  if toolbar[0].is_clicked() == True:
    selected_tool = 'plant'
  elif toolbar[1].is_clicked() == True:
    selected_tool = 'harvest'
  elif toolbar[2].is_clicked() == True:
    selected_tool = 'water'

  #draw tools
  for tool in toolbar:
    tool.draw(tool.x, tool.y, 1, False)
  draw_text(f"Plant", side_menu_font, (0, 0, 0), toolbar[0].x, 770)
  draw_text(f"Harvest", side_menu_font, (0, 0, 0), toolbar[1].x, 770)
  draw_text(f"Water", side_menu_font, (0, 0, 0), toolbar[2].x, 770)

  if selected_tool == 'plant':
    screen.blit(ui_classes.get_image(textures.tool_outline), (toolbar[0].x, toolbar[0].y))
  elif selected_tool == 'harvest':
    screen.blit(ui_classes.get_image(textures.tool_outline), (toolbar[1].x, toolbar[1].y))
  elif selected_tool == 'water':
    screen.blit(ui_classes.get_image(textures.tool_outline), (toolbar[2].x, toolbar[2].y))

  screen.blit(ui_classes.get_image(textures.cash_money), (80, 10))

  screen.blit(ui_classes.get_image(textures.breads_menu), (SCREEN_WIDTH - ui_classes.get_image(textures.breads_menu).get_width(), 10))
  screen.blit(ui_classes.get_image(textures.inventory_menu), (SCREEN_WIDTH - ui_classes.get_image(textures.breads_menu).get_width(), 15 + textures.ui_classes.get_image(textures.breads_menu).get_height()))

  for button in inventory_menu_items:
    button.draw(button.x, button.y, 1, False)

#I know this is really bad programming but I just needa get this done o_o
#I sincerely appologise for the following few blocks of code
  if inventory_menu_items[0].is_clicked():
    selected_seed = "plain_bread"
    inventory_outline.y = inventory_menu_items[0].y
  elif inventory_menu_items[1].is_clicked():
    selected_seed = "bread_monster"
    inventory_outline.y = inventory_menu_items[1].y
  elif inventory_menu_items[2].is_clicked():
    selected_seed = "bread_crab"
    inventory_outline.y = inventory_menu_items[2].y
  elif inventory_menu_items[3].is_clicked():
    selected_seed = "baba_ganoush"
    inventory_outline.y = inventory_menu_items[3].y

  if inventory_menu_items[0].is_clicked():
    selected_seed = "plain_bread"
    inventory_outline.y = inventory_menu_items[0].y
  elif inventory_menu_items[1].is_clicked():
    selected_seed = "bread_monster"
    inventory_outline.y = inventory_menu_items[1].y
  elif inventory_menu_items[2].is_clicked():
    selected_seed = "bread_crab"
    inventory_outline.y = inventory_menu_items[2].y
  elif inventory_menu_items[3].is_clicked():
    selected_seed = "baba_ganoush"
    inventory_outline.y = inventory_menu_items[3].y

  if breads_menu_items[0].is_clicked():
    if test_buyable(inventory["money"], 5):
      inventory["money"] += -5
      inventory["plain_bread"] += 1
  elif breads_menu_items[1].is_clicked():
    if test_buyable(inventory["money"], 30):
      inventory["money"] += -30
      inventory["bread_monster"] += 1
  elif breads_menu_items[2].is_clicked():
    if test_buyable(inventory["money"], 10):
      inventory["money"] += -10
      inventory["bread_crab"] += 1
  elif breads_menu_items[3].is_clicked():
    if test_buyable(inventory["money"], 500):
      inventory["money"] += -500
      inventory["baba_ganoush"] += 1


  save.draw(save.x, save.y, 1, False)
  if save.is_clicked():
    saveloadmanage.save_data(plots, "plots")
    saveloadmanage.save_data(inventory, "inventory")

  inventory_outline.draw(inventory_outline.x, inventory_outline.y, 1, False)

  for index, key in enumerate(inventory):
    if index > 0:
      draw_text(f"{key}: {inventory[key]}", side_menu_font, (255, 255, 255), 950, index*49+450)

  for index, bread in enumerate(breads):
    draw_text(f"{bread}", side_menu_font, (255, 255, 255), 950, index*49+54)

  htp_button.draw(htp_button.x, htp_button.y, 1, False)
  if htp_button.colliding(pygame.mouse.get_pos()):
    screen.blit(ui_classes.get_image(textures.how_to_play), (0, 0))

  for event in pygame.event.get():
    if event == pygame.QUIT:
      run = False
    elif event == pygame.VIDEORESIZE:
      screen = pygame.display.set_mode((event.h, event.v), pygame.RESIZABLE)

  if frame >= 9:
    frame = 0
  else:
    frame += 1

  pygame.display.update()

pygame.quit()
