class HintSystem:
    def provide_hint(self, board):
        # Analyze board and provide hint
        hint_row, hint_col = self.find_easy_hint(board)
        return hint_row, hint_col