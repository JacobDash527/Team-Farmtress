import pygame
import ui_classes
import game_classes
import textures
import pyvidplayer
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

plots = []
plots.append([[1, 1, 'null', 'null', False], [2, 1, 'null', 'null', False], [3, 1, 'null', 'null', False], [4, 1, 'null', 'null', False], [5, 1, 'null', 'null', False]])
plots.append([[1, 2, 'null', 'null', False], [2, 2, 'null', 'null', False], [3, 2, 'null', 'null', False], [4, 2, 'null', 'null', False], [5, 2, 'null', 'null', False]])
plots.append([[1, 3, 'null', 'null', False], [2, 3, 'null', 'null', False], [3, 3, 'null', 'null', False], [4, 3, 'null', 'null', False], [5, 3, 'null', 'null', False]])
plots.append([[1, 4, 'null', 'null', False], [2, 4, 'null', 'null', False], [3, 4, 'null', 'null', False], [4, 4, 'null', 'null', False], [5, 4, 'null', 'null', False]])
plots.append([[1, 5, 'null', 'null', False], [2, 5, 'null', 'null', False], [3, 5, 'null', 'null', False], [4, 5, 'null', 'null', False], [5, 5, 'null', 'null', False]])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('teamfarmtress')
arrow_frame_list = []
frame = 0

intro_vid = pyvidplayer.Video("Mr Pixtel.mp4")
intro_vid.set_size((800, 450))

breads_menu = ui_classes.SideMenus(pygame.image.load("images/breads_button.png").convert_alpha(), pygame.image.load("images/breads_menu.png").convert_alpha())

clock = pygame.time.Clock()

run = True

for xindex, row in enumerate(plots):
  for yindex, column in enumerate(row):
    column[2] = ui_classes.Button(xindex * 90 + 80, yindex * 90 + 125, textures.teleporter, 0.70)

def plot_menu(x, y):
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


#intro()

while run:
  clock.tick(10)

  screen.blit(textures.bg, (0, 0))

  breads_menu.draw()

  for xindex, row in enumerate(plots):
    for yindex, column in enumerate(row):
      column[2].draw(xindex * 90 + 60, yindex * 90 + 125)
      if column[2].colliding(pygame.mouse.get_pos()) == True:
        screen.blit(textures.arrow_sheet.get_image(frame, 15, 23, 4, (0, 0, 0)), (column[2].x + 8, column[2].y - 80))
        if column[2].is_clicked() == True:
          column[4]

  for event in pygame.event.get():
    if event == pygame.QUIT:
      run = False

  if frame >= 9:
    frame = 0
  else:
    frame += 1

  pygame.display.update()

pygame.quit()