from solvers.backtracking_solver import BacktrackingSolver
from visualizer import Visualizer
from hint_system import HintSystem

class SudokuSolver:
    def __init__(self):
        self.solver = BacktrackingSolver()
        self.visualizer = Visualizer()
        self.hint_system = HintSystem()

    def solve(self, board):
        solution = self.solver.solve(board)
        self.visualizer.animate_solution(board, solution)
        return solution

    def provide_hint(self, board):
        return self.hint_system.provide_hint(board)