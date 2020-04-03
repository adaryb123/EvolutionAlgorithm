from possible_solution import Solution
from random import *

class Roulette:
    indexes = []

    def __init__(self,population):
        for solution in population:
            for i in range(solution.get_fitness()):
                self.indexes.insert(0,solution)

    def pick_two(self):
        #first = self.indexes.pop(randint(0,len(self.indexes) - 1))
        #second = self.indexes.pop(randint(0,len(self.indexes) - 1))
        first = self.indexes[randint(0,len(self.indexes) - 1)]
        second = self.indexes[randint(0, len(self.indexes) - 1)]
        return first,second