#Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

main_folder = 'my_project'

print(os.getcwd())
os.chdir('Mikheev_Aleksey_dz_7')
os.mkdir(main_folder)
os.mkdir(os.path.join(main_folder, 'settings'))
os.mkdir(os.path.join(main_folder, 'mainapp'))
os.mkdir(os.path.join(main_folder, 'adminapp'))
os.mkdir(os.path.join(main_folder, 'authapp'))