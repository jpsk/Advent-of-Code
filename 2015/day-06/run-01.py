input_ = open('input.txt', 'r').read().splitlines()

input_split = []
for i in input_:
    input_split.append(i.split(' '))

# define constants
TURN_ON = 1
TURN_OFF = 2
TOGGLE = 3

input_normalized = []
for i in input_split:
    a = []
    if i[0] == 'turn':
        if i[1] == 'on':
            a.append(TURN_ON)
        elif i[1] == 'off':
            a.append(TURN_OFF)
        a.append(i[2].split(','))
        a.append(i[4].split(','))
    if i[0] == 'toggle':
        a.append(TOGGLE)
        a.append(i[1].split(','))
        a.append(i[3].split(','))
    input_normalized.append(a)


grid = []
for x in range(0, 1000):
    for y in range(0, 1000):
        grid.append([x, y, 0])

print('len grid', len(grid))

for i in input_normalized:
    startx = int(i[1][0])
    starty = int(i[1][1])
    endx = int(i[2][0])
    endy = int(i[2][1])

    for x in range(startx, endx+1):
        for y in range(starty, endy+1):
            if i[0] == TURN_OFF:
                grid[x+y*1000][2] = TURN_OFF
            if i[0] == TURN_ON:
                grid[x+y*1000][2] = TURN_ON
            if i[0] == TOGGLE:
                if grid[x+y*1000][2] == 1:
                    grid[x+y*1000][2] = 0
                else:
                    grid[x+y*1000][2] = 1

l = 0

for g in grid:
    if g[2] == 1:
        l += 1

print(l)
