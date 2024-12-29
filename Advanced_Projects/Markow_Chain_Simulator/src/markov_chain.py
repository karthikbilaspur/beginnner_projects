import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.states = len(transition_matrix)

    def simulate(self, initial_state, steps):
        current_state = initial_state
        for _ in range(steps):
            next_state = np.random.choice(self.states, p=self.transition_matrix[current_state])
            current_state = next_state
        return current_state

    def calculate_steady_state(self):
        eigenvalues, eigenvectors = np.linalg.eig(self.transition_matrix.T)
        steady_state = eigenvectors[:, np.isclose(eigenvalues, 1)][:, 0]
        return steady_state / steady_state.sum()