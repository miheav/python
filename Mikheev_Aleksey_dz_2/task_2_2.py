list = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for value in list:
    is_number = False

    for number in numbers:
        if number in value:
            is_number = True

    if(is_number == False):
        new_list.append(value)
    else:
        new_list.append('"')
        new_list.append(value)
        new_list.append('"')

str = ''
previous_is_number = False
is_number = False
for index, value in enumerate(new_list):

    previous_is_number = is_number
    is_number = False

    for number in numbers:
        if number in value:
            is_number = True
    if(is_number):
        str += value
    elif(previous_is_number and value == '"'):
        str += value + " "
    elif(value == '"'):
        str += value
    else:
        str += value + " "

print(list)
print(new_list)
print(str)
