from possible_solution import create_starting_population,breed_and_mutate
from fitness import get_fitness_and_best_solutions
from roulette import Roulette
import matplotlib.pyplot as plt
import copy

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

def make_graph(x_axis,y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel('Generation')
    plt.ylabel('Fitness sum')
    plt.show()

BREEDING_PROBABILITY = 90
MUTATION_PROBABILITY = 5
SOLUTIONS_KEPT = 10
GENERATION_LIMIT = 100

map,height,width,stones_num = get_input()
print_map(map)
population = create_starting_population(height,width)
y_axis = []
x_axis = []
for j in range(GENERATION_LIMIT):
    fitness_sum,best_solutions = get_fitness_and_best_solutions(map,height,width,stones_num,population,SOLUTIONS_KEPT)
    x_axis.append(j)
    y_axis.append(fitness_sum)
    new_population = []
    new_population += best_solutions
    roulette = Roulette(population)
    for i in range(int((GENERATION_LIMIT-SOLUTIONS_KEPT) / 2)):
        first,second = roulette.pick_two()
        breed_and_mutate(first,second,BREEDING_PROBABILITY,MUTATION_PROBABILITY)
        new_population.append(first)
        new_population.append(second)
    population = copy.deepcopy(new_population)

make_graph(x_axis,y_axis)