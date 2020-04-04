from random import *

class Roulette:
    population = []

    def __init__(self,population):          #when roulette is created, every solution from population gets ammount of population based on their fitness
        self.population.clear()
        for solution in population:
            for i in range(solution.get_fitness()):
                self.population.insert(0,solution)

    def pick_two(self):             #function removes 2 random solutions from roulette
        first = self.population[randint(0,len(self.population) - 1)]
        second = self.population[randint(0, len(self.population) - 1)]
        return first,second