input_ = open('input.txt', 'r').read().splitlines()

print('Input q = ', len(input_))

# vowels constrain
vowels = ['a', 'e', 'i', 'o', 'u']
strings_with_vowels = []

for i in input_:
    w = 0
    for s in i:
        if s in vowels:
            w += 1
    if w >= 3:
        strings_with_vowels.append(i)

print('With vowels = ', len(strings_with_vowels))

# doubles constrain
strings_with_doubles = []
for s in strings_with_vowels:
    double = False
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            double = True
    if double is True:
        strings_with_doubles.append(s)

print('With doubles = ', len(strings_with_doubles))

# exceptions constrain
exceptions = ['ab', 'cd', 'pq', 'xy']
strings_with_exceptions = []

for s in strings_with_doubles:
    exception = True
    for e in exceptions:
        if e in s:
            exception = False
    if exception is True:
        strings_with_exceptions.append(s)


print('Without exceptions = ', len(strings_with_exceptions))



