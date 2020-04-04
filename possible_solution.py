from random import *
import random as RANDOM
from collections import OrderedDict

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

    def mutate(self):       #function reshuffles genes in solution chromosome
        RANDOM.shuffle(self.sequence)



def cross_breed(solution1,solution2):           #function breeds 2 solutions by ending quarters
    sequence1 = solution1.get_sequence()
    sequence2 = solution2.get_sequence()
    new_sequence1 = sequence1[:int(len(sequence1)/5 * 4)] + sequence2[int(len(sequence2)/5 * 4):]
    new_sequence2 = sequence2[:int(len(sequence2)/5 * 4)] + sequence1[int(len(sequence1)/5 * 4):]
    solution1.set_sequence(list(OrderedDict.fromkeys(new_sequence1)))
    solution2.set_sequence(list(OrderedDict.fromkeys(new_sequence2)))

def breed_and_mutate(solution1,solution2,breeding_probability,mutation_probability):        #function decides if the solutions will breed and/or mutate
    chance = randint(0,100)
    if chance < breeding_probability:
        cross_breed(solution1,solution2)
    chance = randint(0, 100)
    if chance < mutation_probability:
        solution1.mutate()
    chance = randint(0, 100)
    if chance < mutation_probability:
        solution2.mutate()

def create_starting_population(height,width):           #function creates starting population from random numbers
    max_solution_length = height + width
    starting_points = list(range(0,max_solution_length))
    population = [Solution() for i in range(100)]
    for i in range(100):
       # solution_length = randint(int(max_solution_length/2),max_solution_length-1)
        population[i].set_sequence(sample(starting_points,len(starting_points)))#solution_length))

    return population

def find_best_solution_in_population(population):       #function finds the best solution in the last population
    best = population[0]
    for solution in population:
        if solution.get_fitness() > best.get_fitness():
            best = solution

    return best