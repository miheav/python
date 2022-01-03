#*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs') as f:
    data = []
    spam_dict = {}
    for line in f:
        ip = line[: line.find(" ")]
        new_line = line[line.find('"'):]
        method = new_line[1: new_line.find(' ')]
        request = new_line[new_line.find(' ') + 1: new_line[new_line.find(' ') + 1:].find(' ')]

        data.append((ip,method,request))
        spam_dict.setdefault(ip, 0)
        spam_dict[ip] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[0])  # Not only one spamer