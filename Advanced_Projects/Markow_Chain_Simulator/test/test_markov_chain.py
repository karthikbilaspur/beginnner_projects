import unittest
from markov_chain import MarkovChain

class TestMarkovChain(unittest.TestCase):
    def test_simulate(self):
        transition_matrix = [[0.7, 0.3], [0.4, 0.6]]
        markov_chain = MarkovChain(transition_matrix)
        self.assertEqual(markov_chain.simulate(0, 1), 0 or 1)

if __name__ == '__main__':
    unittest.main()