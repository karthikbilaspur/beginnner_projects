import random

def parse_grid(grid_str):
    # Parse Sudoku grid from string
    grid = []
    for row in grid_str.split('\n'):
        grid.append([int(x) if x != '.' else 0 for x in row.split()])
    return grid

def generate_random_grid():
    # Generate random Sudoku grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            grid[row][col] = random.randint(0, 9)
    return grid

def copy_grid(grid):
    # Copy Sudoku grid
    return [row[:] for row in grid]