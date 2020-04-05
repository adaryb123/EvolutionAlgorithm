from random import *

class Tournament():
    population = []

    def __init__(self,population):
        self.population.clear()
        for solution in population:
            for i in range(solution.get_fitness()):
                self.population.insert(0, solution)

    def compete(self,solution1,solution2,solution3):
        fitness1 = solution1.get_fitness()
        fitness2 = solution2.get_fitness()
        fitness3 = solution3.get_fitness()
        sum = fitness1 + fitness2 + fitness3
        chance1 = int(sum/fitness1 * 100)
        chance2 = chance1 + int(sum/fitness2 * 100)
        chance3 = 100
        result = randint(0,100)
        if result <= chance1:
            return solution1
        elif result <= chance2:
            return solution2
        elif result <= chance3:
            return solution3

    def pick_two(self):
        indexes = list(range(100))
        three_random = sample(indexes,3)
        solution1 = self.population[three_random[0]]
        solution2 = self.population[three_random[1]]
        solution3 = self.population[three_random[2]]
        first = self.compete(solution1,solution2,solution3)

        three_random = sample(indexes, 3)
        two_random = sample(indexes, 2)
        solution1 = self.population[three_random[0]]
        solution2 = self.population[three_random[1]]
        solution3 = self.population[three_random[2]]
        second = self.compete(solution1,solution2,solution3)
        return first,second