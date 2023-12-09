import pygame
pygame.init()


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 70
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, wnd):
        wnd.blit(self.image, (self.hitbox.x, self.hitbox.y))


width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze')

bg = pygame.transform.scale(pygame.image.load('img/bg.png'), (width, height))

fox = Sprite(10, 10, 'img/fox.png')

GameOver = False
while not GameOver:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

    fox.draw(window)

    pygame.display.update()

pygame.quit()
