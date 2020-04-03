import random

class Solution:

    sequence = []
    fitness = 0

    def get_sequence(self):
        return self.sequence

    def get_fitness(self):
        return self.fitness

    def set_fitness(self,fitness):
        self.fitness = fitness

    def set_sequence(self,sequence):
        self.sequence = sequence

    def mutate(self):
        random.shuffle(self.sequence)