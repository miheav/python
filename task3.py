list = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(list)


keep_on = False

for index, value in enumerate(list):

    is_number = False

    for number in numbers:
        if number in list[index]:
            is_number = True

    if(is_number == True and index+2 <= len(list) and list[index - 1] != '"' and list[index + 1] != '"'):
        list.insert(index, '"')
        list.insert(index + 2, '"')

        

print(list)

str = ''
previous_is_number = False
is_number = False
for index, value in enumerate(list):

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


print(str)
