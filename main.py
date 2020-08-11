import pygame
import random
from config import *
pygame.init()

# Store all heights in this
bars = []

# Changing color while selected
global color

# SCREEN
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bubble Sort Visualization")
screen.fill(WHITE)
clock = pygame.time.Clock()

def bubleSort(list):
    listLenght = len(list)
    for i in range(listLenght):
        for j in range(0, listLenght-1-i):
            #Drawing
            for k in range(BARS):
                if bars[k] is bars[j] or bars[k] is bars[j + 1]:
                    color = SELECTED_BAR_COLOR
                else:
                    color = BAR_COLOR

                posX = (k * BAR_WIDTH) + (k * SPACE) + (WIDTH - (BARS * BAR_WIDTH * SPACE)) / 2
                height = bars[k]
                drawBars(posX, height, color)
            # Updating screen    
            pygame.display.update()
            pygame.time.wait(1000)
            screen.fill(WHITE)
            # Buble Sort
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j] 
    # After change all bar color
    color = SORTED_BAR_COLOR
    drawAllBars(bars, color)
    message = "Sorted thanks for waiting"

def drawAllBars(list, color):
    for bar in range(BARS):
        posX = (bar * BAR_WIDTH) + (bar * SPACE) + (WIDTH - (BARS * BAR_WIDTH * SPACE)) / 2
        height = list[bar]
        drawBars(posX, height, color)
        

def drawBars(posX, height, color):
    pygame.draw.rect(screen, color, (posX, 240, BAR_WIDTH, height), 0)
    bars.append(height)

def setBarsHeight():
    for i in range(BARS):
        height = random.randint(-100, -10)
        posX = (i * BAR_WIDTH) + (i * SPACE) + (WIDTH - (BARS * BAR_WIDTH * SPACE)) / 2
        drawBars(posX, height, BAR_COLOR)

setBarsHeight()
bubleSort(bars)
# mainLoop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()