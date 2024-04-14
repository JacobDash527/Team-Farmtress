import pygame
import ui_classes
import game_classes
import textures
import pyvidplayer
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#[x, y, button, plant, menu_open]
plots = []
plots.append([[1, 1, 'null', 'null', False], [2, 1, 'null', 'null', False], [3, 1, 'null', 'null', False], [4, 1, 'null', 'null', False], [5, 1, 'null', 'null', False]])
plots.append([[1, 2, 'null', 'null', False], [2, 2, 'null', 'null', False], [3, 2, 'null', 'null', False], [4, 2, 'null', 'null', False], [5, 2, 'null', 'null', False]])
plots.append([[1, 3, 'null', 'null', False], [2, 3, 'null', 'null', False], [3, 3, 'null', 'null', False], [4, 3, 'null', 'null', False], [5, 3, 'null', 'null', False]])
plots.append([[1, 4, 'null', 'null', False], [2, 4, 'null', 'null', False], [3, 4, 'null', 'null', False], [4, 4, 'null', 'null', False], [5, 4, 'null', 'null', False]])
plots.append([[1, 5, 'null', 'null', False], [2, 5, 'null', 'null', False], [3, 5, 'null', 'null', False], [4, 5, 'null', 'null', False], [5, 5, 'null', 'null', False]])

inventory = {"money":0, "single_harvest_seeds":0, "multi_harvest":0, "seed_dropper":0}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Team Farmtress')
arrow_frame_list = []
frame = 0
text_font = pygame.font.SysFont("ROG Fonts Regular", 30)

# intro_vid = pyvidplayer.Video("Mr Pixtel.mp4")
# intro_vid.set_size((800, 450))

# breads_menu = ui_classes.SideMenus(pygame.image.load("images/breads_button.png").convert_alpha(), pygame.image.load("images/breads_menu.png").convert_alpha())

clock = pygame.time.Clock()

run = True

for xindex, row in enumerate(plots):
  for yindex, column in enumerate(row):
    column[2] = ui_classes.Button(xindex * 90 + 80, yindex * 90 + 125, textures.teleporter, 0.70)

def plant_menu(plot_x, plot_y):
  screen.blit(textures.plant_menu, (plot_x, plot_y))
  x, y = pygame.mouse.get_pos()
  if pygame.mouse.get_pressed()[0] == 1:
    if (plot_y + 27) < y < (plot_y + 40):
      pass
    elif (plot_y + 49) < y < (plot_y + 59):
      pass
    elif (plot_y + 71) < y < (plot_y + 84):
      pass

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

  screen.blit(textures.breads_menu, (548, 20))

  for xindex, row in enumerate(plots):
    for yindex, column in enumerate(row):
      column[2].draw(xindex * 90 + 60, yindex * 90 + 125)

  for xindex, row in enumerate(plots):
    for yindex, column in enumerate(row):
      if column[2].colliding(pygame.mouse.get_pos()):
        screen.blit(textures.arrow_sheet.get_image(frame, 15, 23, 4, (0, 0, 0)), (column[2].x - 10, column[2].y - 80))
        if column[2].is_clicked() == True:
          column[4] = True

      if column[4]:
        print(plant_menu(xindex * 90 + 60, yindex * 90 + 125))

  draw_text("big black cock", text_font, (0, 0, 0), 100, 100)

  for event in pygame.event.get():
    if event == pygame.QUIT:
      run = False

  if frame >= 9:
    frame = 0
  else:
    frame += 1

  pygame.display.update()

pygame.quit()