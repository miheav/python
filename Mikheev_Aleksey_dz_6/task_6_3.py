

from itertools import zip_longest
import json
out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)


file_1 = open('users.csv', 'r', encoding='utf-8')
content = file_1.read()
print(content[0])