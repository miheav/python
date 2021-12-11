cubes = []
for i in range(1, 1001, 2):
    cubes.append(i*i*i)

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
    cube += 17 # Павильная строка
    string = str(cube)
    # string = str(cube + 17) # Можете подсказать почему из за такого подхода ответ был 15392908808 а не 15392909930 как у всех
    sum = 0
    for number in string:
        sum += int(number)
    if(sum % 7 == 0):
        cube_sum += cube

print("Задача b-c, сумма = ",cube_sum)
