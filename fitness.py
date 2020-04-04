from plow_function import plow
import copy

def maximum_possible_fitness(height,width,stones_num):          #function calculates how many empty spaces are in map
    return (height * width) - stones_num

def assign_fitness(empty_map,height,width,stones_num,solution):         #function assigns fitness to a solution
    map = copy.deepcopy(empty_map)
    sequence = solution.get_sequence()
    plow_number = 1
    for i in range(len(sequence)):
        cant_move, plow_number = plow(map,height,width,sequence[i],plow_number)
        if cant_move == False:
            break
    solution.set_fitness(maximum_possible_fitness(height,width,stones_num) - sum(row.count(0) for row in map) )

def add_to_best_solutions(new_solution,best_solutions,solutions_to_keep):       #function adds solution to the best few from population, if it is
    for solution in best_solutions:
        if new_solution.get_sequence() == solution.get_sequence():
            return best_solutions

    for i in range(solutions_to_keep):
        if i == len(best_solutions):
            best_solutions.append(new_solution)
            break

        elif best_solutions[i].get_fitness() < new_solution.get_fitness():
            best_solutions.insert(i,new_solution)
            break

    return best_solutions[:solutions_to_keep]


def get_fitness_and_best_solutions(map,height,width,stones_num,population,solutions_to_keep):   #function assign fitness to whole population and finds best few solutions
    sum = 0
    best_solutions = []
    for solution in population:
        assign_fitness(map,height,width,stones_num,solution)
        sum += solution.get_fitness()
        best_solutions = add_to_best_solutions(solution,best_solutions,solutions_to_keep)

    return sum,best_solutions


