import numpy as np

class TransitionMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = np.random.rand(size, size)
        self.matrix /= self.matrix.sum(axis=1, keepdims=True)

    def edit(self, row, col, value):
        self.matrix[row, col] = value
        self.matrix[row] /= self.matrix[row].sum()