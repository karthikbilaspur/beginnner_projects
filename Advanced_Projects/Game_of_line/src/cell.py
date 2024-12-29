import pygame

class Cell:
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.state = False
        self.next_state = False

    def draw(self, screen):
        if self.state:
            pygame.draw.rect(screen, (255, 255, 255), (self.x * self.cell_size, self.y * self.cell_size, self.cell_size, self.cell_size))