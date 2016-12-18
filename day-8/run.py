import sys, time

input_ = open('input.txt').read().splitlines()


class Parser(object):
    def __init__(self, instructions, verbose=False, matrix_params=(50, 6)):
        self.instructions = instructions
        self.verbose = verbose
        self.matrix = self.reset_matrix(matrix_params)

    @staticmethod
    def reset_matrix(m):
        matrix = []
        for i in range(m[1]):
            row = [" "] * m[0]
            matrix.append(row)
        return matrix

    def print_matrix(self):
        print('+' + '-' * 99 + '+')
        for i in self.matrix:
            print("|" + "|".join(i) + "|")
        print('+' + '-' * 99 + '+')
        sys.stdout.flush()

    def __rect(self, w, h):
        for i in range(w):
            for j in range(h):
                self.matrix[j][i] = "*"

    def __rotate_90(self, backwards=False):
        if backwards:
            self.matrix = [list(a) for a in zip(*self.matrix)][::-1]
        else:
            self.matrix = [list(a) for a in zip(*self.matrix[::-1])]

    def __rotate_h(self, line, n, backwards=False):
        m_line = len(self.matrix[line])
        if backwards:
            self.matrix[line] = self.matrix[line][n % m_line:] + self.matrix[line][:n % m_line:]
            return
        self.matrix[line] = self.matrix[line][-n % m_line:] + self.matrix[line][:-n % m_line]

    def __rotate_v(self, line, n):
        self.__rotate_90()
        self.__rotate_h(line, n, True)
        self.__rotate_90(True)

    def step(self, instruction):
        instruction = instruction.split(' ')
        if instruction[0] == 'rect':
            i = instruction[1].split('x')
            self.__rect(int(i[0]), int(i[1]))
        elif instruction[1] == 'row':
            self.__rotate_h(int(instruction[2][2:]), int(instruction[-1]))
        elif instruction[1] == 'column':
            self.__rotate_v(int(instruction[2][2:]), int(instruction[-1]))

    def parse(self):
        for i in self.instructions:
            self.step(i)
            if self.verbose:
                print("")
                print("Instruction: {}".format(i))
                self.print_matrix()

print('')
print('-----01,02-----')

parser = Parser(input_, True)
parser.parse()

lights = 0
for x in parser.matrix:
    lights += x.count('*')

print("Lights on: {}".format(lights))
