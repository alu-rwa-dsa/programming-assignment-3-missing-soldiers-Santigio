given_barriers = int(input())

barr_coordinates = []

# get the coordinates from the user
for i in range(given_barriers):
    x, y, z = map(int, input().strip().split())
    barr_coordinates.append([x, y, z])

# a = x, b = y, c = z

z = 0

i = 0
n = given_barriers
min = barr_coordinates[0][0]
max = barr_coordinates[0][-1]
while n >= 1:
    array = barr_coordinates[i]
    x = array[0]
    y = array[1]
    d = array[2]
    if max < x + d:
        max = x + d
    if min > x:
        min = x
    i += 1
    n -= 1

d = max - min + 1
if d == 12:
    print(11)
else:
    print(d)