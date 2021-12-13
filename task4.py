list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for string in list:
    worker = string.split()
    name = worker[-1].title()
    print(f'Привет, {name}!')