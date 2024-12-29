class Board:
    def __init__(self, grid):
        self.grid = grid

    def is_empty(self, row, col):
        return self.grid[row][col] == 0

    def is_valid(self, row, col, num):
        # Check row, column, and box
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for x in range(3):
            for y in range(3):
                if self.grid[box_row + x][box_col + y] == num:
                    return False
        return True

    def place_number(self, row, col, num):
        self.grid[row][col] = num

    def remove_number(self, row, col):
        self.grid[row][col] = 0

    def print(self):
        for row in self.grid:
            print(row)

    def get_possibilities(self, row, col):
        possibilities = []
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                possibilities.append(num)
        return possibilities

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True