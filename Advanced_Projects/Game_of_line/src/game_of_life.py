import pygame
from grid import Grid
from neighbor_detector import NeighborDetector

class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.neighbor_detector = NeighborDetector()
        self.generation = 0

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.grid.width * self.grid.cell_size, self.grid.height * self.grid.cell_size))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.grid.update(self.neighbor_detector)
            self.generation += 1
            self.grid.draw(screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()