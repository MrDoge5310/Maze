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


class Player(Sprite):
    def __init__(self, x, y, filename):
        super().__init__(x, y, filename)
        self.step = 5

    def move_right(self):
        self.hitbox.x += self.step

    def move_left(self):
        self.hitbox.x -= self.step

    def move_up(self):
        self.hitbox.y -= self.step

    def move_down(self):
        self.hitbox.y += self.step


class Enemy(Sprite):
    def __init__(self, x, y, filename):
        super().__init__(x, y, filename)


width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze')

bg = pygame.transform.scale(pygame.image.load('img/bg.png'), (width, height))

player = Player(0, 0, 'img/fox.png')
enemy = Enemy(730, 530, 'img/bunny.png')

GameOver = False
while not GameOver:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move_right()

            if event.key == pygame.K_LEFT:
                player.move_left()

            if event.key == pygame.K_UP:
                player.move_up()

            if event.key == pygame.K_DOWN:
                player.move_down()

    player.draw(window)
    enemy.draw(window)

    pygame.display.update()

pygame.quit()
