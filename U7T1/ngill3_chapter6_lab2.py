from math import ceil

import pygame
from pygame.color import THECOLORS

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()

BOX_SIZE = 16

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(THECOLORS['black'])

    for y in range(ceil(size[1] / BOX_SIZE)):
        for x in range(ceil(size[0] / BOX_SIZE)):
            rect = ((x * BOX_SIZE) + 1, (y * BOX_SIZE) + 1, BOX_SIZE - 2, BOX_SIZE - 2)
            pygame.draw.rect(screen, THECOLORS['green'], rect)

    pygame.display.flip()
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
