class BruteForceSolver:
    def solve(self, board):
        for num in range(1, 10):
            for row in range(9):
                for col in range(9):
                    if board.is_empty(row, col):
                        board.place_number(row, col, num)
                        if self.solve(board):
                            return True
                        board.remove_number(row, col)
        return False