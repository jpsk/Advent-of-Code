input_ = open('input.txt').read()


class Parser(object):
    def __init__(self, archived_string):
        self.archived_string = archived_string
        self.pointer = 0
        self.marker = ''
        self.unarchived_string = ''

    def increment_pointer(self, val=1):
        self.pointer += val

    def execute_marker(self):
        _marker = self.marker.split('x')
        _start = self.pointer
        _end = self.pointer + int(_marker[0])
        _string_to_multiply = self.archived_string[_start:_end]
        _string_to_add = _string_to_multiply * int(_marker[1])
        _pointer_jump = int(_marker[0])
        self.unarchived_string += _string_to_add
        self.marker = ''
        self.increment_pointer(_pointer_jump)

    def cur_char(self):
        return self.archived_string[self.pointer]

    def read_marker(self):
        self.increment_pointer()
        while self.cur_char() != ')':
            self.marker = self.marker + self.archived_string[self.pointer]
            self.increment_pointer()
        self.increment_pointer()
        print('Marker is read: {}'.format(self.marker))

    def parse(self):
        while self.pointer != len(self.archived_string):
            if self.cur_char() == '(':
                self.read_marker()
                self.execute_marker()
            else:
                self.unarchived_string += self.cur_char()
                self.increment_pointer()


parser = Parser(input_)
parser.parse()

print('\n-----01-----')
print('Length: {}'.format(len(parser.unarchived_string)))

print('\n-----02-----')


def extract(sequence):
    count = 0
    if '(' not in sequence:
        return len(sequence)
    while '(' in sequence:
        count += sequence.find('(')
        sequence = sequence[sequence.find('('):]
        marker = list(map(int, sequence[1:sequence.find(')')].split('x')))
        sequence = sequence[sequence.find(')') + 1:]
        count += extract(sequence[:marker[0]]) * marker[1]
        sequence = sequence[marker[0]:]
    count += len(sequence)
    return count

print('Length: {}'.format(extract(input_)))