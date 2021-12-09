cubes = [3*3*3, 7*7*7, 23*23*23, 101*101*101, 19*19*19]
# задача а
cube_sum = 0
for cube in cubes:
    string = str(cube)
    sum = 0
    for number in string:
        sum += int(number)
    if(sum % 7 == 0 and sum > 0):
        cube_sum += cube

print("Задача а, сумма = " + str(cube_sum))

# задача b-c
cube_sum = 0
for cube in cubes:
    string = str(cube + 17)
    sum = 0
    for number in string:
        sum += int(number)
    if(sum % 7 == 0 and sum > 0):
        cube_sum += cube

print("Задача b-c, сумма = " + str(cube_sum))