input_ = open('input.txt', 'r').read().splitlines()

print('Input q = ', len(input_))


def constrain1(string):
    for x in range(len(string)-1):
        if string[x:x+2] in string[x+2:]:
            return True
    return False


def constrain2(string):
    for x in range(len(string)-2):
        if string[x] == string[x+2]:
            return True
    return False


c1 = []
for i in input_:
    if constrain1(i):
        c1.append(i)

c2 = []
for i in c1:
    if constrain2(i):
        c2.append(i)

print(len(c2))




