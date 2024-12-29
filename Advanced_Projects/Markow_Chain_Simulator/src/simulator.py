import matplotlib.pyplot as plt

class Simulator:
    def __init__(self, markov_chain):
        self.markov_chain = markov_chain

    def run(self, initial_state, steps):
        final_state = self.markov_chain.simulate(initial_state, steps)
        return final_state

    def visualize_probability_distribution(self, steps):
        probabilities = [self.markov_chain.calculate_steady_state()]
        for _ in range(steps):
            probabilities.append(self.markov_chain.simulate(0, 1))
        plt.bar(range(self.markov_chain.states), [p for p in probabilities])
        plt.xlabel('State')
        plt.ylabel('Probability')
        plt.show()