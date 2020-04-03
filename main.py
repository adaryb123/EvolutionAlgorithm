from plow_function import plow
from possible_solution import Solution
import copy
from random import *
from collections import OrderedDict

def get_input():
    height = int(input("Enter heighth: "))
    width = int(input("Enter width: "))
    map =  [[0 for i in range(width)] for i in range(height)]
    stones_num = int(input("Enter number of stones: "))
    for i in range(stones_num):
        x = int(input("Enter row of stone "+ str(i+1) + " : "))
        y = int(input("Enter column of stone "+ str(i+1) + " : "))
        map[x][y] = -1
    print("All stones saved")
    return map,height,width,stones_num

def print_map(map):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map]))
    print("_________________")


def fitness(empty_map,height,width,stones_num,solution):
    map = copy.deepcopy(empty_map)
    sequence = solution.get_sequence()
    for i in range(len(sequence)):
        if plow(map,height,width,sequence[i],i+1) == False:
            break
    solution.set_fitness((height * width) - sum(row.count(0) for row in map) - stones_num)

def add_to_best5(solution,best5):
    for i in range(5):
        if i == len(best5):
            best5.append(solution)
            break

        elif best5[i].get_fitness() < solution.get_fitness():
            best5.insert(i,solution)
            break

    return best5[:5]

def average_fitness_and_best5(map,height,width,stones_num,population):
    sum = 0
    best5 = []
    for solution in population:
        fitness(map,height,width,stones_num,solution)
        sum += solution.get_fitness()
        best5 = add_to_best5(solution,best5)

    return sum / 100,best5

def create_starting_population(height,width):
    max_solution_length = height + width
    starting_points = list(range(0,max_solution_length))
    population = [Solution() for i in range(100)]
    for i in range(100):
        solution_length = randint(1,max_solution_length-1)
        population[i].set_sequence(sample(starting_points,solution_length))

    return population

def cross_breed(solution1,solution2):
    sequence1 = solution1.get_sequence()
    sequence2 = solution2.get_sequence()
    new_sequence1 = sequence1[:int(len(sequence1)/2)] + sequence2[int(len(sequence2)/2):]
    new_sequence2 = sequence2[:int(len(sequence2) / 2)] + sequence1[int(len(sequence1) / 2):]
    solution1.set_sequence(list(OrderedDict.fromkeys(new_sequence1)))
    solution2.set_sequence(list(OrderedDict.fromkeys(new_sequence2)))


map,height,width,stones_num = get_input()
population = create_starting_population(height,width)
population_fitness,best5 = average_fitness_and_best5(map,height,width,stones_num,population)
