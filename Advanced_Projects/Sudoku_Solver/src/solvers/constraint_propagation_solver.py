class ConstraintPropagationSolver:
    def solve(self, board):
        while True:
            changed = False
            for row in range(9):
                for col in range(9):
                    if board.is_empty(row, col):
                        possibilities = board.get_possibilities(row, col)
                        if len(possibilities) == 1:
                            board.place_number(row, col, possibilities[0])
                            changed = True
            if not changed:
                break
        return board.is_solved()