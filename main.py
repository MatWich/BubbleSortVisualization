import pygame
import random
from config import *
pygame.init()

# SCREEN
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bubble Sort Visualization")
screen.fill(WHITE)

def drawBars(posX, height):
    pygame.draw.rect(screen, BAR_COLOR, (posX, 360, BAR_WIDTH, height), 0)

def setBarsHeight():
    for i in range(BARS):
        height = random.randint(-100, -10)
        posX = (i * BAR_WIDTH) + (i * SPACE)
        drawBars(posX, height)

setBarsHeight()
# mainLoop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()