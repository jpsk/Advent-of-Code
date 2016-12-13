input_ = open('input.txt').read().splitlines()

merged_input = "".join(input_)

message_signal = []
for i in range(len(input_[0])):
    message_signal.append("".join(merged_input[i::len(input_[0])]))

list_abc_map = []

for i in range(len(message_signal)):
    char_abc_map = []
    for x in list(map(chr, range(97, 123))):
        if x in message_signal[i]:
            char_abc_map.append((x, message_signal[i].count(x)))
    list_abc_map.append(char_abc_map)

print('')
print('-----01-----')

for i in range(len(list_abc_map)):
    biggest = list_abc_map[i][0]
    for j in range(len(list_abc_map[i])):
        list__ = list_abc_map[i][j]
        if list__[1] > biggest[1]:
            biggest = list_abc_map[i][j]
    print("Biggest {}".format(biggest))


print('')
print('-----02-----')

for i in range(len(list_abc_map)):
    smallest = list_abc_map[i][0]
    for j in range(len(list_abc_map[i])):
        list__ = list_abc_map[i][j]
        if list__[1] < smallest[1]:
            smallest = list_abc_map[i][j]
    print("Smallest {}".format(smallest))





