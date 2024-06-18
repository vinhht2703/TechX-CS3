import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Hello Pygame !!")
x = 100
co = True

redSurface = pygame.Surface((50, 50))
redSurface.fill((255, 0, 0))

# # khung hình load
rectSurface = pygame.Surface((100, 100))
rectSurface.fill((128, 0, 128))

# rectSurface.blit(redSurface, (50, 50))
# # vẽ khung lên khung giao diện chính

rectRed = redSurface.get_rect(topleft=(50, 100))
rectPur = rectSurface.get_rect(topleft=(100, 100))

# vòng lặp game vô tận
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    DISPLAYSURF.fill((255, 255, 255))  # Red Green Blue

    # pygame.draw.rect(DISPLAYSURF, (128, 0, 128), (100, 20, 150, 50))

    if rectRed.colliderect(rectPur):
        rectSurface.fill((255, 255, 0))
    else:
        rectSurface.fill((128, 0, 128))

    DISPLAYSURF.blit(redSurface, rectRed)
    DISPLAYSURF.blit(rectSurface, rectPur)

    if co:
        rectRed.x += 5
    else:
        rectRed.x -= 5

    if rectRed.x >= 750:
        co = False

    if rectRed.x <= 0:
        co = True

    pygame.display.update()
    pygame.time.Clock().tick(60)  # FPS