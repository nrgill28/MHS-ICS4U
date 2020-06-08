import random

import pygame
from pygame.color import THECOLORS

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()

snow = [
    (random.randint(0, 640), random.randint(0, 480))
    for _ in range(50)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((81, 207, 232))

    # Draw the ground
    pygame.draw.rect(screen, THECOLORS['white'], (0, 440, 640, 480))

    # Draw the snowman's body
    y_pos = 420
    r = 40
    for i in range(3):
        pygame.draw.circle(screen, THECOLORS['white'], (320, y_pos), r)
        y_pos -= int(r * 1.25)
        r = int(r / 1.3)
    r = int(r * 1.3)
    y_pos += int(r / 1.25)

    # Draw the snowman's eyes
    pygame.draw.circle(screen, THECOLORS['black'], (310, y_pos), 4)
    pygame.draw.circle(screen, THECOLORS['black'], (330, y_pos), 4)

    # Draw the snowman's nose
    pygame.draw.polygon(
        screen, THECOLORS['orange'],
        [
            (320, y_pos + 15),
            (317, y_pos + 4),
            (323, y_pos + 4)
        ], 0
    )

    # Draw the snow
    for i in range(len(snow)):
        # For each particle, draw a circle in it's position then update it's position
        particle = snow[i]
        pygame.draw.circle(screen, THECOLORS['white'], particle, 3)
        snow[i] = (particle[0] + random.randint(-1, 1), particle[1] + 1)

        # If it fell off the screen, reset it
        if snow[i][1] > 480:
            snow[i] = (random.randint(0, 640), 0)

    pygame.display.flip()
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
