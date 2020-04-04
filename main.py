from possible_solution import create_starting_population,breed_and_mutate,find_best_solution_in_population
from fitness import get_fitness_and_best_solutions,maximum_possible_fitness
from roulette import Roulette
import matplotlib.pyplot as plt
import copy
from plow_function import plow

def get_input():                #function loads starting parameter from input
    height = int(input("Enter heighth: "))
    width = int(input("Enter width: "))
    map =  [[0 for i in range(width)] for i in range(height)]
    stones_num = int(input("Enter number of stones: "))
    for i in range(stones_num):
        x = int(input("Enter row of stone "+ str(i+1) + " : "))
        y = int(input("Enter column of stone "+ str(i+1) + " : "))
        map[x][y] = -1
    print("All stones saved")
    print("Empty map looks like this: ")
    print_map(map)
    return map,height,width,stones_num

def print_map(map):             #function prints game map as matrix
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map]))

def make_graph(x_axis,y_axis):          #function makes simple graph using matplotlib
    plt.plot(x_axis, y_axis)
    plt.xlabel('Generation')
    plt.ylabel('Fitness sum')
    plt.show()

def print_result(population,maximum_possible_fitness,x_axis,y_axis):            #function prints result in the end
    best_solution = find_best_solution_in_population(population)
    best_sequence = best_solution.get_sequence()
    print("Algorithm ended")
    print("Best solution from the last generation is : ")
    for i in range(len(best_sequence)):
        if plow(map,height,width,best_sequence[i],i+1) == False:
            break
    print_map(map)
    print("With fitness "+ str(best_solution.get_fitness()) + " out of maximum fitness " + str(maximum_possible_fitness))
    see_graph = input("Do you wanna see the graph of population fitness over time? Y/N :  ")
    if see_graph == "Y" or see_graph == "y":
        make_graph(x_axis, y_axis)

BREEDING_PROBABILITY = 90
MUTATION_PROBABILITY = 5
SOLUTIONS_KEPT = 10
GENERATION_LIMIT = 100

map,height,width,stones_num = get_input()
population = create_starting_population(height,width)
maximum_possible_fitness = maximum_possible_fitness(height,width,stones_num)
y_axis = []
x_axis = []
for j in range(GENERATION_LIMIT):
    print("Generation: " + str(j))
    fitness_sum,best_solutions = get_fitness_and_best_solutions(map,height,width,stones_num,population,SOLUTIONS_KEPT)
    x_axis.append(j)
    y_axis.append(fitness_sum)
    new_population = []
    new_population += best_solutions
    roulette = Roulette(population)
    for i in range(int((100-SOLUTIONS_KEPT) / 2)):
        first,second = roulette.pick_two()
        breed_and_mutate(first,second,BREEDING_PROBABILITY,MUTATION_PROBABILITY)
        new_population.append(first)
        new_population.append(second)
    population = copy.deepcopy(new_population)

print_result(population,maximum_possible_fitness,x_axis,y_axis)