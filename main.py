from possible_solution import Solution
from random import *
from collections import OrderedDict
from fitness import get_fitness_and_best4
from roulette import Roulette

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

def create_starting_population(height,width):
    max_solution_length = height + width
    starting_points = list(range(0,max_solution_length))
    population = [Solution() for i in range(100)]
    for i in range(100):
        solution_length = randint(int(max_solution_length/2),max_solution_length-1)
        population[i].set_sequence(sample(starting_points,solution_length))

    return population

def cross_breed(solution1,solution2):
    sequence1 = solution1.get_sequence()
    sequence2 = solution2.get_sequence()
    new_sequence1 = sequence1[:int((len(sequence1)/2)+1)] + sequence2[int((len(sequence2)/2)-1):]
    new_sequence2 = sequence2[:int((len(sequence2)/2)+1)] + sequence1[int((len(sequence1)/2)-1):]
    solution1.set_sequence(list(OrderedDict.fromkeys(new_sequence1)))
    solution2.set_sequence(list(OrderedDict.fromkeys(new_sequence2)))

def breed_and_mutate(solution1,solution2,breeding_probability,mutation_probability):
    chance = randint(0,100)
    if chance <= breeding_probability:
        cross_breed(solution1,solution2)
    chance = randint(0, 100)
    if chance <= mutation_probability:
        solution1.mutate()
    chance = randint(0, 100)
    if chance <= mutation_probability:
        solution2.mutate()

def print_population(population,fitness_sum):
    #for solution in population:
     #  print(solution.get_sequence())
     #  print(solution.get_fitness())

    print("TOTAL FITNESS: "+str(fitness_sum))
    print("________________________________________________________________")

BREEDING_PROBABILITY = 90
MUTATION_PROBABILITY = 5

map,height,width,stones_num = get_input()
population = create_starting_population(height,width)
for j in range(100):
    fitness_sum,best4 = get_fitness_and_best4(map,height,width,stones_num,population)
    print_population(population,fitness_sum)
    new_population = []
    new_population += best4
    roulette = Roulette(population)
    for i in range(48):
        first,second = roulette.pick_two()
        #print(len(first.get_sequence()))
       #print(len(second.get_sequence()))
        breed_and_mutate(first,second,BREEDING_PROBABILITY,MUTATION_PROBABILITY)
       # print(len(first.get_sequence()))
       # print(len(second.get_sequence()))
      #  print("_______________________________________________")
        new_population.append(first)
        new_population.append(second)
    population = new_population

for solution in population:
     print(solution.get_sequence())
     print(solution.get_fitness())