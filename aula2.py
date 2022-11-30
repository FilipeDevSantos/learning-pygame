import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((800, 680))
pygame.display.set_caption('Desenhando na tela')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0, 255, 2), (20, 300, 40, 100))
    pygame.draw.circle(tela, (255, 0, 0), (400, 340), 20)
    pygame.draw.rect(tela, (0, 255, 2), (740, 300, 40, 100))

    pygame.display.update()
