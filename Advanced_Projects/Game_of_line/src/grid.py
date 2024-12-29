import pygame

class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = [[Cell(x, y, cell_size) for y in range(height)] for x in range(width)]

    def update(self, neighbor_detector):
        for row in self.cells:
            for cell in row:
                cell.next_state = neighbor_detector.detect(cell, self.cells)
        for row in self.cells:
            for cell in row:
                cell.state = cell.next_state

    def draw(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)