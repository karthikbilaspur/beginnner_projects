import random

class GeneticAlgorithmSolver:
    def solve(self, board):
        population_size = 100
        population = []
        for _ in range(population_size):
            individual = self.generate_individual(board)
            population.append(individual)
        while True:
            population = self.evolve_population(population)
            best_individual = max(population, key=self.fitness)
            if self.fitness(best_individual) == 1:
                board.apply_solution(best_individual)
                return True