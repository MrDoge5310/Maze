import pygame
pygame.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze')

bg = pygame.transform.scale(pygame.image.load('img/bg.png'), (width, height))
window.blit(bg, (0, 0))
