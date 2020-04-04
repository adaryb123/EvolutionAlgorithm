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

def is_index_starting(x,y,starting_x,starting_y):
    return (x==starting_x) and (y == starting_y)

def plow(map, height, width, starting_row_or_column, plow_num):         #function plows the map from starting point, going in straight line, turning right at obstacles
    configuration = get_starting_configuration(starting_row_or_column, height, width)

    if configuration == "DOWN":
        starting_x = 0
        starting_y = starting_row_or_column  # mozno starting column -1 ?
    elif configuration == "LEFT":
        starting_x = starting_row_or_column - width
        starting_y = width - 1
    available_directons = 4
    first_step = True
    current_x = 0
    current_y = 0
    last_configuration = configuration
    while is_index_in_map(current_x, current_y, height, width):
        if first_step:
            if configuration == "DOWN":
                starting_x -= 1
            elif configuration == "LEFT":
                starting_y += 1
            current_x = starting_x
            current_y = starting_y
            first_step = False

        if available_directons == 0:
            return False

        # move down if possible
        if configuration == "DOWN":
            if last_configuration == "UP":
                configuration = "LEFT"
                available_directons -= 1

            next_x = current_x + 1
            next_y = current_y
          #  if is_index_starting(current_x,current_y,starting_x,starting_y):
          #      configuration = "LEFT"
          #      available_directons -= 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_x = next_x
                available_directons = 4
                last_configuration = configuration
            else:
                configuration = "LEFT"
                available_directons -= 1
            continue

        # move left if possible
        if configuration == "LEFT":
            if last_configuration == "RIGHT":
                configuration = "UP"
                available_directons -= 1
            next_x = current_x
            next_y = current_y - 1
          #  if is_index_starting(current_x,current_y,starting_x,starting_y):
          #      configuration = "UP"
          #      available_directons -= 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_y = next_y
                available_directons = 4
                last_configuration = configuration
            else:
                configuration = "UP"
                available_directons -= 1
            continue

        # move up if possible
        if configuration == "UP":
            if last_configuration == "DOWN":
                configuration = "RIGHT"
                available_directons -= 1
            next_x = current_x - 1
            next_y = current_y
         #   if is_index_starting(current_x,current_y,starting_x,starting_y):
         #       configuration = "RIGHT"
         #       available_directons -= 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_x = next_x
                available_directons = 4
                last_configuration = configuration
            else:
                configuration = "RIGHT"
                available_directons -= 1
            continue

        # move right if possible
        if configuration == "RIGHT":
            if last_configuration == "LEFT":
                configuration = "DOWN"
                available_directons -= 1
            next_x = current_x
            next_y = current_y + 1
        #    if is_index_starting(current_x,current_y,starting_x,starting_y):
        #        configuration = "DOWN"
        #        available_directons -= 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_y = next_y
                available_directons = 4
                last_configuration = configuration
            else:
                configuration = "DOWN"
                available_directons -= 1
            continue

    return True
