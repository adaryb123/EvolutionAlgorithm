
def get_input():
    height = int(input("Enter heighth :"))
    width = int(input("Enter width: "))
    map =  [[0 for i in range(width)] for i in range(height)]
    stone_num = int(input("Enter number of rocks: "))
    for i in range(stone_num):
        x = int(input("Enter row of stone "+ str(i+1) + " : "))
        y = int(input("Enter column of stone "+ str(i+1) + " : "))
        map[x][y] = -1
    print("All stones saved")
    return map,height,width

def print_map(map):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in map]))

def move_down(map,height,width,starting_column,plow_number):
    if map[0][starting_column] != 0:            #toto neviem ci treba
        return False

    x = 0
    y = starting_column
    while x < height and y < width:
        if map[x+1][y] == 0: ##move down
            map[x+1][y] = plow_number
            x += 1
        else:
            if map[x][y+1] == 0:    ##move right?
                map[x][y+1] ==
#move budu separatne funkcie pre vsetky styri smery, vzdy posunu iba o 1


map,height,width = get_input()
print_map(map,height,width)