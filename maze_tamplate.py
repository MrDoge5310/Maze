import random
import pygame


class Maze:
    def __init__(self, width, height):
        self.block_size = 80

        self.maze = []
        for y in range(height // self.block_size):
            row = []
            for x in range(width // self.block_size - 1):
                # Создаем проходы и стены случайным образом
                if random.random() < 0.6:
                    row.append(0)  # 0 представляет проход
                else:
                    row.append(1)  # 1 представляет стену
            self.maze.append(row)

    def drawMaze(self, screen):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size)
                if cell == 1:
                    pygame.draw.rect(screen, 'yellow', rect)

