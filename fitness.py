from plow_function import plow
import copy

def assign_fitness(empty_map,height,width,stones_num,solution):
    map = copy.deepcopy(empty_map)
    sequence = solution.get_sequence()
    for i in range(len(sequence)):
        if plow(map,height,width,sequence[i],i+1) == False:
            break
    solution.set_fitness((height * width) - sum(row.count(0) for row in map) - stones_num)

def add_to_best_solutions(solution,best_solutions,solutions_to_keep):
    for i in range(solutions_to_keep):
        if i == len(best_solutions):
            best_solutions.append(solution)
            break

        elif best_solutions[i].get_fitness() < solution.get_fitness():
            best_solutions.insert(i,solution)
            break

    return best_solutions[:solutions_to_keep]

def get_fitness_and_best_solutions(map,height,width,stones_num,population,solutions_to_keep):
    sum = 0
    best_solutions = []
    for solution in population:
        assign_fitness(map,height,width,stones_num,solution)
        sum += solution.get_fitness()
        best_solutions = add_to_best_solutions(solution,best_solutions,solutions_to_keep)

    return sum,best_solutions
