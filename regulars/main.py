from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding= 'utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r"(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(доб\.)*\s*(\d+)*\)*"
pattern_repl = r"+7(\2)\3-\4-\5 \6\7"

i = 1
for el in contacts_list:
    while i < len(contacts_list):
        res = re.sub(pattern, pattern_repl, contacts_list[i][5])
        contacts_list[i][5] = res
        i += 1
    break

n = 1
for name in contacts_list:
    while n < len(contacts_list):
        name_list = contacts_list[n][0].split()
        if len(name_list) == 3:
            contacts_list[n][0] = name_list[0]
            contacts_list[n][1] = name_list[1]
            contacts_list[n][2] = name_list[2]
        if len(name_list) == 2:
            contacts_list[n][0] = name_list[0]
            contacts_list[n][1] = name_list[1]
        n += 1
    break

k = 1
for name in contacts_list:
    while k < len(contacts_list):
        name_list = contacts_list[k][1].split()
        if len(name_list) == 2:
            contacts_list[k][1] = name_list[0]
            contacts_list[k][2] = name_list[1]
        k += 1
    break

y = 0
m = 1
p = 1

for p in range(len(contacts_list)-1):
    for m in range(len(contacts_list)-1):
        if p != m and contacts_list[p][0] == contacts_list[m][0]:
            for y in range(len(contacts_list[p]) - 1):
                if contacts_list[p][y] == '':
                   contacts_list[p][y] = contacts_list[m][y]
                y += 1
            contacts_list.remove(contacts_list[m])
        m += 1
    p += 1

pprint(contacts_list)

with open("phonebook.csv", "w", encoding= 'utf-8' ) as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)