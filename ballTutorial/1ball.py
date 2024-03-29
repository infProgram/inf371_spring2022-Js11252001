from drawItem import *
import sys, pygame
from item import *
pygame.init()

size = width, height = 640, 480
faceSpeed = [2, 2]
ballSpeed = [1, 1]
gray = (156, 156, 156)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", [2,2], size[0], size[1])
face = Item("smiley.png", [1,1], size[0], size[1])
xball = drawItem([1,1], size[0], size[1], screen)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  ball.move()
  face.move()

  screen.fill(white)
  xball.drawBall((255, 0, 0), [60, 250], 40)
  xball.move()

  screen.blit(ball.object, ball.rect)
  screen.blit(face.object, face.rect)
  pygame.display.flip()