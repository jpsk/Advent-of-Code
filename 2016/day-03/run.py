raw = open('input.txt').readlines()

triangles = []
sorted_triangles = []

for r in raw:
    a = int(r[:5])
    b = int(r[5:10])
    c = int(r[10:])

    triangles.append([a, b, c])
    sorted_triangles.append(sorted([a, b, c]))

print('')
print('-----01-----')

good_triangles = 0

for t in sorted_triangles:
    if t[0] + t[1] > t[2]:
        good_triangles += 1

print('Valid triangles count: {}'.format(good_triangles))

print('')
print('-----02-----')

vertical_array = []

array_idx = 0
array_idx_z = 0

matrix = []
for t in triangles:
    array_idx += 1
    for i in t:
        matrix.append(i)
    if array_idx % 3 == 0:
        vertical_array.append(sorted(matrix[0:9:3]))
        vertical_array.append(sorted(matrix[1:10:3]))
        vertical_array.append(sorted(matrix[2:11:3]))
        array_idx = 0
        matrix = []

good_triangles = 0
for t in vertical_array:
    if t[0] + t[1] > t[2]:
        good_triangles += 1

print('Valid triangles count: {}'.format(good_triangles))
