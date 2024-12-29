class BacktrackingSolver:
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board.is_empty(row, col):
                    for num in range(1, 10):
                        if board.is_valid(row, col, num):
                            board.place_number(row, col, num)
                            if self.solve(board):
                                return True
                            board.remove_number(row, col)
                    return False
        return True