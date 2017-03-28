q = open('input.txt', 'r').read().splitlines()


""" PART 1 """

a = []
for x in q:
    a += [x.split('x')]

sq = 0

for x in a:
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    mid_ = 0
    min_ = min([a, b, c])
    if min_ == a:
        mid_ = min(b, c)
    if min_ == b:
        mid_ = min(a, c)
    if min_ == c:
        mid_ = min(a, b)

    sq += 2*(a*b + a*c + b*c) + min_ * mid_

print(sq)

""" PART 2 """

a = []
for x in q:
    a += [x.split('x')]

pr = 0
rb = 0

for x in a:
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    mid_ = 0
    min_ = min([a, b, c])
    if min_ == a:
        mid_ = min(b, c)
    if min_ == b:
        mid_ = min(a, c)
    if min_ == c:
        mid_ = min(a, b)
    rb += a*b*c
    pr += (min_ + mid_) * 2

print(pr+rb)