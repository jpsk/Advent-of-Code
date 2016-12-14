# input_ = open('test_input.txt').read().splitlines()
input_ = open('input.txt').read().splitlines()

print('')
print('-----01-----')

input_ = list([i.replace('[', " ").replace(']', " ") for i in input_])
input_ = list([i.split(" ") for i in input_])


def abba_positive(str_):
    for j in range(len(str_) - 3):
        if str_[j] == str_[j + 3] and str_[j + 1] == str_[j + 2] and str_[j] != str_[j + 1]:
            return True
    return False


valid_ips = 0

for i in input_:
    abba_in_hypernet = False
    abba_in_sequence = False

    for j in i:
        if i.index(j) % 2 == 0 and abba_positive(j):
            abba_in_sequence = True
        elif abba_positive(j):
            abba_in_hypernet = True

    if abba_in_sequence and not abba_in_hypernet:
        valid_ips += 1

print("Valid IP's: {}".format(valid_ips))

print('')
print('-----02-----')

supports_ssl = 0

def get_aba(str_):
    aba = []
    for i in range(len(str_) - 2):
        if str_[i] == str_[i + 2] and str_[i] != str_[i + 1]:
            aba.append(str_[i:i + 3])
    return aba


def ssl_positive(h_abalist, s_abalist):
    reversed_h_abalist = []
    for h in h_abalist:
        entry = h[1] + h[0] + h[1]
        reversed_h_abalist.append(entry)

    if reversed_h_abalist and s_abalist:
        if set(reversed_h_abalist) & set(s_abalist):
            return True
    return False


for i in input_:
    s_aba_list = []
    h_aba_list = []
    for j in i:
        if i.index(j) % 2 == 0:
            s_aba_list.append(get_aba(j))
        else:
            h_aba_list.append(get_aba(j))

    # flatten lists
    s_aba_list_flattened = sum(s_aba_list, [])
    h_aba_list_flattened = sum(h_aba_list, [])

    if ssl_positive(h_aba_list_flattened, s_aba_list_flattened):
        supports_ssl += 1

print("Entires that support SSL: {}".format(supports_ssl))
