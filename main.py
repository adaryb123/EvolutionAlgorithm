from plow_function import plow
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


def fitness(empty_map,height,width,stones_num,solution):
    map = copy.deepcopy(empty_map)
    for i in range(len(solution)):
        if plow(map,height,width,solution[i],i+1) == False:
            break
    return ((height * width) - sum(row.count(0) for row in map) - stones_num)


map,height,width,stones_num = get_input()
fitness(map,height,width,stones_num,[1,3,2,9])