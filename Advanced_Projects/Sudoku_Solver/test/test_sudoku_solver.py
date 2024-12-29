import unittest
from sudoku_solver import SudokuSolver
from board import Board

class TestSudokuSolver(unittest.TestCase):
    def test_backtracking_solver(self):
        grid_str = "5...3.7....\n6....14.9...\n.....8...\n8.9.7.....\n4.15.6....\n.....3.2.8\n.....8.....\n...3.1.9.6\n....7...4.5"
        grid = parse_grid(grid_str)
        board = Board(grid)
        solver = SudokuSolver()
        self.assertTrue(solver.solve(board))

    def test_constraint_propagation_solver(self):
        grid_str = "4...2.3....\n...1.5.4...\n...3.2.1...\n2...6.8...\n...9.7.5...\n...1.3.4...\n5...8.2....\n...6.9.3..."
        grid = parse_grid(grid_str)
        board = Board(grid)
        solver = SudokuSolver()
        self.assertTrue(solver.solve(board))

    def test_dancing_links_solver(self):
        grid_str = "8...3.2....\n...9.1.4...\n...5.7.6...\n4...3.8...\n...2.9.1...\n...6.5.3...\n...1.8.9...\n2...4.7..."
        grid = parse_grid(grid_str)
        board = Board(grid)
        solver = SudokuSolver()
        self.assertTrue(solver.solve(board))

if __name__ == '__main__':
    unittest.main()