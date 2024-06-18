import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Hello Pygame !!")


class TRex:
    def __init__(self):
        self.x = 20
        self.y = 360
        self.surface = pygame.Surface((55, 43), pygame.SRCALPHA)
        self.surface.blit(
            pygame.image.load("./pygame/img/tRex.png"), (0, 0), (80, 0, 40, 43)
        )
        self.option = 2

        self.timeSkip = 0
        self.time = 5

        self.jump = False
        self.high = 20

    def update(self, left, right, down, up):
        self.surface.fill((0, 0, 0, 0))
        if up:
            self.jump = True
        else:
            self.jump = False

        if self.jump:
            if self.high >= -20:
                self.y -= self.high
                self.high -= 1
            else:
                self.jump = False
                self.high = 20

        if down:
            if self.timeSkip <= self.time:  # 0 - 5
                self.option = 4
            elif self.timeSkip <= self.time * 2:  # 6 - 10
                self.option = 5

        else:
            if self.timeSkip <= self.time:  # 0 - 5
                self.option = 0
            elif self.timeSkip <= self.time * 2:  # 6 - 10
                self.option = 1

        if self.timeSkip > self.time * 2:
            self.timeSkip = 0

        if left:
            self.x -= 2
            self.timeSkip += 1
        if right:
            self.x += 2
            self.timeSkip += 1

        # if down:
        #     self.option= 4

        self.animate()

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def animate(self):
        if self.option == 0:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (0, 0, 40, 43)
            )
        if self.option == 1:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (40, 0, 40, 43)
            )
        if self.option == 2:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (80, 0, 40, 43)
            )
        if self.option == 3:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (120, 0, 40, 43)
            )
        if self.option == 4:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (160, 0, 55, 43)
            )
        if self.option == 5:
            self.surface.blit(
                pygame.image.load("./pygame/img/tRex.png"), (0, 0), (215, 0, 55, 43)
            )


class Ground:
    def __init__(self):
        self.x = 0
        self.y = 400
        self.surface = pygame.Surface((1200, 12), pygame.SRCALPHA)
        self.surface.blit(
            pygame.image.load("./pygame/img/ground.png"), (0, 0, 1200, 12)
        )

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


def main():
    ground = Ground()
    tRex = TRex()
    up, down, left, right = False, False, False, False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True

            if event.type == KEYUP:
                if event.key == K_UP:
                    up = False
                if event.key == K_DOWN:
                    down = False
                if event.key == K_LEFT:
                    left = False
                if event.key == K_RIGHT:
                    right = False

        DISPLAYSURF.fill((255, 255, 255))

        ground.draw()
        tRex.draw()

        tRex.update(left, right, down, up)

        pygame.display.update()
        pygame.time.Clock().tick(60)


main()
