# open input
input_ = open('input.txt', 'r').read()

input_santa = input_[::2]
input_robot = input_[1::2]

print(input_[:20])
print(input_santa[:10])
print(input_robot[:10])


# define rules
SOUTH = 'v'
NORTH = '^'
EAST = '>'
WEST = '<'


class Santa(object):
    def __init__(self):
        self.position = [0, 0]

    def move(self, coord):
        if coord == SOUTH:
            self.position[1] -= 1
        elif coord == NORTH:
            self.position[1] += 1
        elif coord == EAST:
            self.position[0] += 1
        elif coord == WEST:
            self.position[0] -= 1
        else:
            print('Invalid coordinate')


class Map(object):
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    houses = [[0, 0, 1]]

    def __init__(self):
        pass

    def add_house(self, house):
        self.houses.append(house)


map_ = Map()
santa = Santa()
robot = Santa()

for i in input_santa:
    santa.move(i)

    if not (santa.position in ([x[0], x[1]] for x in map_.houses)):
        map_.add_house([santa.position[0], santa.position[1], 1])

for i in input_robot:
    robot.move(i)
    if not (robot.position in ([x[0], x[1]] for x in map_.houses)):
        map_.add_house([robot.position[0], robot.position[1], 1])


print('Visited houses:', len(map_.houses))
