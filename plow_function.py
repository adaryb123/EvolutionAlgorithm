def is_index_in_map(x, y, max_x, max_y):
    if x < max_x and x >= 0 and y < max_y and y >= 0:
        # if map[x][y] = 0:
        return True
    return False


def is_index_empty(map, x, y):
    if map[x][y] == 0:
        return True
    return False


def get_starting_configuration(i, height, width):
    if i >= 0 and i < width:
        return "DOWN"
    elif i >= width and i < (width + height):
        return "LEFT"
    else:
        return "UNKNOWN CONFIGURATION"


def plow(map, height, width, starting_row_or_column, plow_num):
    configuration = get_starting_configuration(starting_row_or_column, height, width)

    if configuration == "DOWN":
        current_x = 0
        current_y = starting_row_or_column  # mozno starting column -1 ?
    elif configuration == "LEFT":
        current_x = starting_row_or_column - width
        current_y = width - 1
    available_directons = 4
    first_step = True

    while is_index_in_map(current_x, current_y, height, width):
        # print_map(map)
        if first_step:
            if configuration == "DOWN":
                current_x -= 1
            elif configuration == "LEFT":
                current_y += 1
            first_step = False

        if available_directons == 0:
            return False

        # move down if possible
        if configuration == "DOWN":
            next_x = current_x + 1
            next_y = current_y
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_x = next_x
                available_directons = 4
            else:
                configuration = "LEFT"
                available_directons -= 1
            continue

        # move left if possible
        if configuration == "LEFT":
            next_x = current_x
            next_y = current_y - 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_y = next_y
                available_directons = 4
            else:
                configuration = "UP"
                available_directons -= 1
            continue

        # move up if possible
        if configuration == "UP":
            next_x = current_x - 1
            next_y = current_y
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_x = next_x
                available_directons = 4
            else:
                configuration = "RIGHT"
                available_directons -= 1
            continue

        # move right if possible
        if configuration == "RIGHT":
            next_x = current_x
            next_y = current_y + 1
            if is_index_in_map(next_x, next_y, height, width) == False:
                break
            if is_index_empty(map, next_x, next_y):
                map[next_x][next_y] = plow_num
                current_y = next_y
                available_directons = 4
            else:
                configuration = "DOWN"
                available_directons -= 1
            continue

    return True
