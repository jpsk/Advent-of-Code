instructions = open('input.txt').readlines()

print(len(instructions))


class Keypad(object):
    def __init__(self):
        self.cur_key = 5
        self.keypad_matrix_v = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.keypad_matrix_h = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def move(self, m):
        if m == 'U':
            if self.cur_key in self.keypad_matrix_v[0]:
                pass
            else:
                self.cur_key -= 3
        elif m == 'D':
            if self.cur_key in self.keypad_matrix_v[2]:
                pass
            else:
                self.cur_key += 3
        elif m == 'R':
            if self.cur_key in self.keypad_matrix_h[2]:
                pass
            else:
                self.cur_key += 1
        elif m == 'L':
            if self.cur_key in self.keypad_matrix_h[0]:
                pass
            else:
                self.cur_key -= 1


keypad = Keypad()

for x in range(len(instructions)):
    for y in instructions[x]:
        keypad.move(y)
    print('No {} digit is: {} '.format(x, keypad.cur_key))
