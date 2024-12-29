import random

def generate_random_grid(width, height):
    # Generate random grid configuration
    grid = [[random.choice([True, False]) for _ in range(width)] for _ in range(height)]
    return grid

def save_pattern(grid, filename):
    # Save grid pattern to file
    with open(filename, 'w') as f:
        for row in grid:
            f.write(''.join(['*' if cell else '.' for cell in row]) + '\n')

def load_pattern(filename):
    # Load grid pattern from file
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            grid.append([cell == '*' for cell in line.strip()])
    return grid