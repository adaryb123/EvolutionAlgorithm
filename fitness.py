from plow_function import plow
import copy

def assign_fitness(empty_map,height,width,stones_num,solution):
    map = copy.deepcopy(empty_map)
    sequence = solution.get_sequence()
    for i in range(len(sequence)):
        if plow(map,height,width,sequence[i],i+1) == False:
            break
    solution.set_fitness((height * width) - sum(row.count(0) for row in map) - stones_num)

def add_to_best4(solution,best4):
    for i in range(4):
        if i == len(best4):
            best4.append(solution)
            break

        elif best4[i].get_fitness() < solution.get_fitness():
            best4.insert(i,solution)
            break

    return best4[:4]

def get_fitness_and_best4(map,height,width,stones_num,population):
    sum = 0
    best4 = []
    for solution in population:
        assign_fitness(map,height,width,stones_num,solution)
        sum += solution.get_fitness()
        best4 = add_to_best4(solution,best4)

    return sum,best4
