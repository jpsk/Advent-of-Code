import hashlib

i = 0
found = 0

# first
print('')
print('-----01-----')
while True:
    i += 1
    input_ = ('ugkcyxxp' + str(i)).encode()
    hash_ = hashlib.md5(input_)
    if hash_.hexdigest()[:5] == '00000':
        found += 1
        print('Found {}: {} hex: {} at pos: {}'.format(found, hash_.hexdigest()[5], hash_.hexdigest(), i))
    if found == 8:
        break

# second
print('')
print('-----02-----')
found_positions = []
while True:
    i += 1
    input_ = ('ugkcyxxp' + str(i)).encode()
    hash_ = hashlib.md5(input_)
    hex = hash_.hexdigest()
    if hex[:5] == '00000' and 48 <= ord(hex[5]) <= 57:
        if int(hex[5]) in range(8) and (int(hex[5]) not in found_positions):
            found_positions.append(int(hex[5]))
            print('Found {}: {} hex: {} at pos : {}'.format(int(hex[5]) + 1, hex[6], hex, i - 1))

    if len(found_positions) == 8:
        break
