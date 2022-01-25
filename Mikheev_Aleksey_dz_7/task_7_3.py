# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil

print(os.getcwd())
os.chdir('Mikheev_Aleksey_dz_7')

root = 'my_project'

if not os.path.exists(os.path.join(os.path.abspath(root), 'templates')):
    os.mkdir(os.path.join(os.path.abspath(root), 'templates'))

for r, d, f in os.walk(root):
    split = os.path.split(r)
    copy_folder = split[1]
    template_folder = os.path.basename(split[0])
    if(template_folder != 'templates'):
        continue
    if not os.path.exists(os.path.join(os.path.abspath(root), 'templates', copy_folder)):
        os.mkdir(os.path.join(os.path.abspath(root), 'templates', copy_folder))
    for file in f:
        if not os.path.exists(os.path.join(os.path.abspath(root), 'templates', copy_folder, file)):
            shutil.copy(os.path.join(os.path.abspath(r), file), os.path.join(os.path.abspath(root), 'templates', copy_folder, file))
    