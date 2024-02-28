import pygame
import time
import classes

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('FNAP')
bread_monster = pygame.transform.scale(pygame.image.load("images/teleporter.png"), (100, 100))
bg = pygame.image.load("images/bg.png").convert_alpha()
arrow_sheet = classes.SpriteSheet(pygame.image.load("sprite_sheets/arrow_sheet.png"))
arrow_frame_list = []
frame = 0

clock = pygame.time.Clock()
button = classes.Button(400, 300, bread_monster)

run = True

while run:
  clock.tick(10)

  screen.blit(bg, (0, 0))

  button.draw()

  if button.colliding(pygame.mouse.get_pos()) == True:
    screen.blit(arrow_sheet.get_image(frame, 15, 23, 4, (0, 0, 0)), (button.x + 20, button.y - 100))

  for event in pygame.event.get():
    if event == pygame.QUIT:
      run = False

  pygame.display.update()

  if frame >= 9:
    frame = 0
  else:
    frame += 1

pygame.quit()