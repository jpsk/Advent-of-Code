instructions = open('input.txt').read().split(', ')

# Vectors

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

current_vector = NORTH
current_location = [0, 0]


def change_vector(curr_pos, instruct_pos):
    if instruct_pos == 'L':
        if curr_pos == NORTH:
            return WEST
        return curr_pos - 1
    elif instruct_pos == 'R':
        if curr_pos == WEST:
            return NORTH
        return curr_pos + 1


for i in instructions:
    current_vector = change_vector(current_vector, i[0])
    inted_i = int(i[1:])

    if current_vector == NORTH:
        current_location[1] += inted_i
    elif current_vector == EAST:
        current_location[0] += inted_i
    elif current_vector == SOUTH:
        current_location[1] -= inted_i
    elif current_vector == WEST:
        current_location[0] -= inted_i

print(current_location)


# part2


class Map(object):
    def __init__(self):
        self.map_ = [[0, 0]]
        self.visited = 0
        self.first_location = None

    def add_to_map(self, val):
        if val not in self.map_:
            self.map_.append(val)
        else:
            self.visited = 1
            self.first_location = val


current_vector = NORTH
current_location = [0, 0]
map_ = Map()
break_ = 0
for i in instructions:
    current_vector = change_vector(current_vector, i[0])
    inted_i = int(i[1:])

    if break_ == 1:
        break

    for x in range(inted_i):
        if current_vector == NORTH:
            current_location[1] += 1
        elif current_vector == EAST:
            current_location[0] += 1
        elif current_vector == SOUTH:
            current_location[1] -= 1
        elif current_vector == WEST:
            current_location[0] -= 1

        if map_.visited == 0:
            map_.add_to_map(list(current_location))

        else:
            print('FIRST ::: {}'.format(map_.first_location))
            break_ = 1
            break
