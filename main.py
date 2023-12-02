import pygame
pygame.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze')

bg = pygame.transform.scale(pygame.image.load('img/bg.png'), (width, height))


GameOver = False
while not GameOver:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

    pygame.display.update()

pygame.quit()
