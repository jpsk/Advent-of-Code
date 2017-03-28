import numpy

instructions = open('input.txt').readlines()

print('')
print('-----01-----')


class Keypad(object):
    def __init__(self):
        self.cur_key = 5
        self.keypad = numpy.arange(1, 10).reshape(3, 3)

    def col(self, n):
        return self.keypad[:, n]

    def move(self, m):
        if m == 'U' and self.cur_key not in self.keypad[0]:
            self.cur_key -= 3
        elif m == 'D' and self.cur_key not in self.keypad[2]:
            self.cur_key += 3
        elif m == 'R' and self.cur_key not in self.col(2):
            self.cur_key += 1
        elif m == 'L' and self.cur_key not in self.col(0):
            self.cur_key -= 1


keypad = Keypad()

for x in range(len(instructions)):
    for y in instructions[x]:
        keypad.move(y)
    print('No {} digit is: {} '.format(x + 1, keypad.cur_key))

# v2
print('')
print('-----02-----')


class NewKeypad(object):
    def __init__(self):
        self.cur_pos = [2, 0]
        self.keypad = numpy.array([
            ['-', '-', '1', '-', '-'],
            ['-', '2', '3', '4', '-'],
            ['5', '6', '7', '8', '9'],
            ['-', 'A', 'B', 'C', '-'],
            ['-', '-', 'D', '-', '-']])

    def getval(self, row, col):
        val = self.keypad[row, col]
        return val

    def move(self, m):
        xx = self.cur_pos[0]
        yy = self.cur_pos[1]

        if m == 'U' and xx != 0:
            if self.getval(self.cur_pos[0] - 1, yy) != '-':
                self.cur_pos[0] -= 1
        elif m == 'D' and xx != 4:
            if self.getval(self.cur_pos[0] + 1, yy) != '-':
                self.cur_pos[0] += 1
        elif m == 'L' and yy != 0:
            if self.getval(xx, self.cur_pos[1] - 1) != '-':
                self.cur_pos[1] -= 1
        elif m == 'R' and yy != 4:
            if self.getval(xx, self.cur_pos[1] + 1) != '-':
                self.cur_pos[1] += 1


new_keypad = NewKeypad()

for x in range(len(instructions)):
    for y in instructions[x]:
        new_keypad.move(y)
    print('No {} digit is: {} '.format(x + 1, new_keypad.keypad[new_keypad.cur_pos[0], new_keypad.cur_pos[1]]))
