import pygame
import ui_classes
import game_classes
import textures
import time

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

#[x, y, plant, plot_button, menu_open]
plots = []
plots.append([[0, 0, 'null', 'null', False], [0, 1, 'null', 'null', False], [0, 2, 'null', 'null', False], [0, 3, 'null', 'null', False], [0, 4, 'null', 'null', False]])
plots.append([[1, 0, 'null', 'null', False], [1, 1, 'null', 'null', False], [1, 2, 'null', 'null', False], [1, 3, 'null', 'null', False], [1, 4, 'null', 'null', False]])
plots.append([[2, 0, 'null', 'null', False], [2, 1, 'null', 'null', False], [2, 2, 'null', 'null', False], [2, 3, 'null', 'null', False], [2, 4, 'null', 'null', False]])
plots.append([[3, 0, 'null', 'null', False], [3, 1, 'null', 'null', False], [3, 2, 'null', 'null', False], [3, 3, 'null', 'null', False], [3, 4, 'null', 'null', False]])
plots.append([[4, 0, 'null', 'null', False], [4, 1, 'null', 'null', False], [4, 2, 'null', 'null', False], [4, 3, 'null', 'null', False], [4, 4, 'null', 'null', False]])

inventory = {"money":20, "single_harvest":4, "multi_harvest":0, "seed_dropper":0}

# plant_button = ui_classes
# harvest_button = ui_classes
# water_button = ui_classes

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Team Farmtress')
arrow_frame_list = []
frame = 0
text_font = pygame.font.SysFont("ROG Fonts Regular", 60)

selected_seed = 'single_harvest'
selected_tool = ''
toolbar = [ui_classes.Button(50, 1050, textures.plant, 0.7), ui_classes.Button(250, 1050, textures.harvester, 0.7), ui_classes.Button(450, 1050, textures.watering_can, 0.7)]

# intro_vid = pyvidplayer.Video("Mr Pixtel.mp4")
# intro_vid.set_size((800, 450))

clock = pygame.time.Clock()

run = True

for xindex, row in enumerate(plots):
  for yindex, column in enumerate(row):
    column[3] = ui_classes.Button(xindex * 180 + 120, yindex * 180 + 100, textures.teleporter, 1.4)
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

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#intro()

while run:
  clock.tick(10)

  screen.blit(textures.bg, (0, 0))

  #screen.blit(textures.breads_menu, (1096, 40))

  for xindex, row in enumerate(plots):
    for yindex, column in enumerate(row):
      column[3].draw(xindex * 180 + 120, yindex * 180 + 100, 1, False)
      if column[2] != "null":
        column[2].tick()
        column[3].enabled = False
        column[2].draw(xindex, yindex)
        column[2].tick
        if column[2].button.colliding(pygame.mouse.get_pos()):
          pass

      #use tools
      if column[3].is_clicked():
        #plant tool
        if selected_tool == 'plant':
          if inventory['single_harvest'] >= 1 :
            column[2] = game_classes.SeedDropper(1, 100, "single_harvest", xindex, yindex, textures.bread_monster)
            inventory['single_harvest'] += -1
      
      if column[2] != "null":
        if column[2].button.is_clicked():
          #harvest tool
          if selected_tool == 'harvest':
            harvest_data = column[2].harvest()
            if column[2].type == 'multi_harvest':
              pass
            else:
              inventory['money'] += harvest_data[0]
              inventory[column[2].type] += harvest_data[1]
              column[2] = 'null'
              column[3].enabled = True
          elif selected_tool == 'water':
            column[2].water()        

      if column[3].colliding(pygame.mouse.get_pos()):
        screen.blit(textures.arrow_sheet.get_image(frame, 15, 50, 8, (0, 0, 0)), (column[3].x+18, column[3].y-180))

  draw_text(f"${inventory['money']}", text_font, (255, 255, 255), 100, 25)

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

  if selected_tool == 'plant':
    screen.blit(textures.tool_outline, (toolbar[0].x, toolbar[0].y))
  elif selected_tool == 'harvest':
    screen.blit(textures.tool_outline, (toolbar[1].x, toolbar[1].y))
  elif selected_tool == 'water':
    screen.blit(textures.tool_outline, (toolbar[2].x, toolbar[2].y))

  screen.blit(textures.cash_money, (10, 10))

  #screen.blit(textures.breads_menu, (0, 0))

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