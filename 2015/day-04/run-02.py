
import hashlib

secret = open("input.txt", 'r').read()

iso = True
number = 0

while iso:
    s = secret + str(number)
    a = hashlib.md5(s.encode('utf')).hexdigest()[:6]
    if a == '000000':
        iso = False
        print(number)
    number += 1
