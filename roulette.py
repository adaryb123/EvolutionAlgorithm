from random import *

class Roulette:
    indexes = []

    def __init__(self,population):          #when roulette is created, every solution from population gets ammount of indexes based on their fitness
        self.indexes.clear()
        for solution in population:
            for i in range(solution.get_fitness()):
                self.indexes.insert(0,solution)

    def pick_two(self):             #function removes 2 random solutions from roulette
        first = self.indexes[randint(0,len(self.indexes) - 1)]
        second = self.indexes[randint(0, len(self.indexes) - 1)]
        return first,second