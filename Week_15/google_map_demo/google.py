import pygame
import sys
import random
from pygame.locals import *
import json
from dijkstra import Graph

# Đọc file JSON
with open("./data.json", "r") as file:
    data = json.load(file)

graph = Graph()
graph.load_from_json(data)

WINDOWWIDTH = 1720
WINDOWHEIGHT = 980


pygame.init()
pygame.display.set_caption("map")
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
DISPLAYSURF.fill((255, 255, 255))


def check_key_in_data(user_key, data):
    for item in data:
        if item["key"] == user_key:
            return item
    return None


font_size = 24
font = pygame.font.Font(None, font_size)  # Sử dụng font mặc định của Pygame


def main():

    color = []
    path = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if len(color) >= 2:
                    color = []

                for item in data:
                    locat = pygame.Surface((30, 30))
                    locat_pos = (item["X"], item["Y"])
                    rect = locat.get_rect(topleft=locat_pos)

                    if rect.collidepoint(mouse_pos):
                        if item not in color:
                            color.append(item)

        background_image = pygame.image.load("./img/map.png")
        background_image = pygame.transform.scale(
            background_image, (WINDOWWIDTH, WINDOWHEIGHT)
        )
        DISPLAYSURF.blit(background_image, (0, 0))

        if len(color) == 2:
            keys = graph.dijkstra(color[0]["key"], color[1]["key"])
            lenKeys = len(keys)
            for i in range(lenKeys):
                if i + 1 < lenKeys:
                    point = check_key_in_data(keys[i], data)
                    nextPoint = check_key_in_data(keys[i + 1], data)
                    pygame.draw.line(
                        DISPLAYSURF,
                        (0, 255, 0),
                        (point["X"] + 15, point["Y"] + 15),
                        (nextPoint["X"] + 15, nextPoint["Y"] + 15),
                        10,
                    )

        for item in data:
            locat = pygame.Surface((30, 30))

            text_surface = font.render(str(item["key"]), True, (0, 0, 0))

            if check_key_in_data(item["key"], color):
                locat.fill((255, 255, 0))
            else:
                locat.fill((255, 0, 0))

            locat.blit(text_surface, (10, 10))
            locat_pos = (item["X"], item["Y"])
            DISPLAYSURF.blit(locat, locat_pos)

        pygame.display.update()
        pygame.time.Clock().tick(60)


main()
