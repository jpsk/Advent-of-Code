instructions = open('input.txt').read()



print('')
print('-----01-----')

floor = 0
charpos = 0
found = False

for i in instructions:
    if floor == -1:
        found = True

    if i == '(':
        floor += 1
    else:
        floor -= 1


    if not found:
        charpos += 1


print(floor)


print('')
print('-----02-----')
print(charpos)