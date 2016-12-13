input_ = open('input.txt').readlines()


def parse_checksum(value):
    return value.rstrip().split('[')[1][:-1]


def parse_sector(value):
    val = int(value.rstrip().split('-')[-1].split('[')[0])
    return val


def parse_name(value):
    return "-".join(value.rstrip().split('-')[:-1])


def generate_checksum(value):
    abc_map = []
    for x in list(map(chr, range(97, 123))):
        abc_map.append((x, value.count(x)))

    sorted_ = []
    for x in range(5):
        biggest = ('-', -1)
        for y in abc_map:
            if y[1] not in sorted_:
                if y[1] > biggest[1] or y[1] == biggest[1] and ord(y[0]) < ord(biggest[0]):
                    biggest = y
        sorted_.append(biggest)
        abc_map.pop(abc_map.index(biggest))
    return "".join(list(z[0] for z in sorted_))


def validate_checksum(i_name, i_checksum):
    if generate_checksum(i_name) == i_checksum:
        return True
    return False


sum_sector = 0
for i in input_:
    name = parse_name(i)
    checksum = parse_checksum(i)
    sector = parse_sector(i)
    generated_checksum = generate_checksum(i)

    if validate_checksum(name, checksum):
        sum_sector += parse_sector(i)

print('')
print('-----01-----')
print('Sum: {}'.format(sum_sector))

print('')
print('-----02-----')
input_ = open('input.txt').readlines()

filtered_input = []
for i in input_:
    if validate_checksum(parse_name(i), parse_checksum(i)):
        filtered_input.append(i)

for i in filtered_input:
    sector = parse_sector(i)
    name = parse_name(i)
    decoded_name = ""
    for x in name:
        if x == '-':
            decoded_name += ' '
        else:
            new_char = ord(x) + sector
            while new_char > 122:
                new_char -= 26
            decoded_name += chr(new_char)
    if 'pole' in decoded_name:
        print('The sector you are looking for is: {}'.format(sector))



