# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru


# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

import re

def email_parse(email):
    regex = r'^([a-z0-9_-]+)@([a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})$'
    REGEX = re.compile(regex)
    print(email)
    res = REGEX.findall(email)
    dict = {'user': '', 'domain': ''}
    if(res):
        dict['user'] = res[0][0]
        dict['domain'] = res[0][1]
    else:
        raise ValueError('Email невалиден')
    
    print(dict)


email_parse('someone@geekbrains.ru')