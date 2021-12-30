# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

tuple_list = []
with open('nginx_logs', 'r', encoding='utf-8') as file_1:
   for line in file_1:
       line = line.splitlines()[0]
       ip = line[: line.find(" ")]
       new_line = line[line.find('"'):]
       method = new_line[1: new_line.find(' ')]
       request = new_line[new_line.find(' ') + 1: new_line[new_line.find(' ') + 1:].find(' ')]
    #    print(ip)
    #    print(method)
    #    print(request)
    #    print(line)
       tuple_list.append((ip, method, request))


print(tuple_list)