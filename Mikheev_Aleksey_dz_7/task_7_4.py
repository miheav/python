# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import shutil

print(os.getcwd())
os.chdir('Mikheev_Aleksey_dz_7')

dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0,
}


root = 'my_project'

for r, d, f in os.walk(root):

    if(f):
        for file in f:
            size = os.stat(os.path.join(r,file)).st_size

            if(size <= 100):
                dict[100] += 1
            elif size <= 1000:
                dict[1000] += 1
            elif size <= 10000:
                dict[10000] += 1
            elif size <= 100000:
                dict[100000] += 1

print(dict)