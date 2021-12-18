# Задание А
print('Задаие А')
list = [57.8, 46.51, 97, 13, 22.54, 95.12, 102, 99, 85, 43, 45.56, 205.01]
print(list)
for value in list:
    string = str(value)
    str_list = string.split('.')
    roubles = str_list[0]
    if(len(str_list) > 1):
        kopeys = str_list[1]
    else:
        kopeys = '0'
    kopeys = int(kopeys)

    print(f'{roubles} руб {kopeys:02d} коп')


print()

# Задание B

print('Задание B')
print(list)
list_id = id(list)
print('id списка', list_id)
list.sort()
print(list)
for good in list:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ') 

print('id оригинала:', list_id, 'id отсортиранного списка:',
      id(list), 'Списки равны:', list_id == id(list))
print()

# Задание C
print('Задание C')
print(list)
new_list = sorted(list, reverse=True)
for good in new_list:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ') 
print()

# Задание D
print('Задание D')
list = [57.8, 46.51, 97, 13, 22.54, 95.12, 102, 99, 85, 43, 45.56, 205.01]
list = sorted(list, reverse=True)
for good in sorted(list, reverse=True)[:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой

