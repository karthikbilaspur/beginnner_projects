import unittest
from game_of_life import GameOfLife
from grid import Grid
from cell import Cell

class TestGameOfLife(unittest.TestCase):
    def test_grid_initialization(self):
        grid = Grid(10, 10, 10)
        self.assertEqual(grid.width, 10)
        self.assertEqual(grid.height, 10)

    def test_cell_initialization(self):
        cell = Cell(0, 0, 10)
        self.assertFalse(cell.state)

    def test_neighbor_detection(self):
        grid = Grid(3, 3, 10)
        grid.cells[0][0].state = True
        detector = NeighborDetector()
        neighbors = detector.count_neighbors(grid.cells[0][0], grid)
        self.assertEqual(neighbors, 0)

    def test_game_of_life_run(self):
        game = GameOfLife(10, 10, 10)
        game.run()

if __name__ == '__main__':
    unittest.main()