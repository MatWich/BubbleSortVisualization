import pygame
import random
from config import *
pygame.init()

bars = []

# SCREEN
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bubble Sort Visualization")
screen.fill(WHITE)

def bubleSort(list):
    listLenght = len(list)
    for i in range(listLenght):
        for j in range(0, listLenght-1-i):
            
            #Drawing
            for k in range(BARS):
                posX = (i * BAR_WIDTH) + (i * SPACE) + (WIDTH - (BARS * BAR_WIDTH * SPACE)) / 2
                height = bars[k]
                drawBars(posX, height)
                pygame.display.update()
                pygame.time.wait(1)
            # Buble Sort
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j] 


def drawBars(posX, height):
    pygame.draw.rect(screen, BAR_COLOR, (posX, 240, BAR_WIDTH, height), 0)
    bars.append(height)

def setBarsHeight():
    for i in range(BARS):
        height = random.randint(-100, -10)
        posX = (i * BAR_WIDTH) + (i * SPACE) + (WIDTH - (BARS * BAR_WIDTH * SPACE)) / 2
        drawBars(posX, height)

setBarsHeight()
bubleSort(bars)
# mainLoop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()