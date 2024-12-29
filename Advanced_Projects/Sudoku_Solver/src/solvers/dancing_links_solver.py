class DancingLinksSolver:
    def solve(self, board):
        # Initialize dancing links matrix
        matrix = []
        for row in range(9):
            for col in range(9):
                for num in range(1, 10):
                    if board.is_valid(row, col, num):
                        matrix.append((row, col, num))
        # Perform dancing links algorithm
        solution = self.dancing_links(matrix)
        board.apply_solution(solution)
        return board.is_solved()