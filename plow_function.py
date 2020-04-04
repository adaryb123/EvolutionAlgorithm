def is_index_in_map(x, y, max_x, max_y):        #function checks if the index is valid
    if x < max_x and x >= 0 and y < max_y and y >= 0:
        return True
    return False


def is_index_empty(map, x, y):              #function checks if the index is available
    if map[x][y] == 0:
        return True
    return False


def get_starting_configuration(i, height, width):       #function returns corresponding configuration from starting from row or column
    if i >= 0 and i < width:
        return "DOWN"
    elif i >= width and i < (width + height):
        return "LEFT"
    else:
        return "UNKNOWN CONFIGURATION"

def is_index_starting(x,y,starting_x,starting_y):       #function checks if the index is index of staring row or column
    return (x == starting_x) and (y == starting_y)

def turn(available_turns,configuration):
    if available_turns == 2:
        if configuration == "DOWN":
            configuration = "LEFT"
        elif configuration == "RIGHT":
            configuration = "DOWN"
        elif configuration == "UP":
            configuration = "RIGHT"
        elif configuration == "LEFT":
            configuration = "UP"
            available_turns -= 1
    elif available_turns == 1:
        if configuration == "LEFT":
            configuration = "RIGHT"
        elif configuration == "UP":
            configuration = "DOWN"
        elif configuration == "RIGHT":
            configuration = "LEFT"
        elif configuration == "DOWN":
            configuration = "UP"
            available_turns -= 1
    elif available_turns == 0:
        configuration = "END"
    return available_turns,configuration

def plow(map, height, width, starting_row_or_column, plow_num):         #function plows the map from starting point, going in straight line, turning right at obstacles

    configuration = get_starting_configuration(starting_row_or_column, height, width)
    if configuration == "DOWN":
        starting_x = 0
        starting_y = starting_row_or_column  
    elif configuration == "LEFT":
        starting_x = starting_row_or_column - width
        starting_y = width - 1

    if is_index_empty(map,starting_x,starting_y) == False:      #neviem ci tu ma byt return True alebo False
        return True,plow_num
    else:
        map[starting_x][starting_y] = plow_num

    current_x = starting_x
    current_y = starting_y
    available_turns = 2
    while(is_index_in_map(current_x,current_y, height, width)):
        if configuration == "DOWN":
            current_x += 1
        elif configuration == "UP":
            current_x -= 1
        elif configuration == "LEFT":
            current_y -= 1
        elif configuration == "RIGHT":
            current_y += 1
        elif configuration == "END":
            return False,plow_num


        if is_index_in_map(current_x,current_y, height, width) == False:
            break
        else:
            if is_index_empty(map,current_x,current_y):
                map[current_x][current_y] = plow_num
                available_turns = 2
            else:
                if configuration == "DOWN":
                    current_x -= 1
                elif configuration == "UP":
                    current_x += 1
                elif configuration == "LEFT":
                    current_y += 1
                elif configuration == "RIGHT":
                    current_y -= 1
                available_turns,configuration = turn(available_turns,configuration)
    return True,plow_num+1
