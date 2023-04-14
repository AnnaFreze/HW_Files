import os

lines = []
files = []
names = []
names_dict = {}
files_dict = {}

with open('sorted/1.txt', 'rt', encoding = 'utf-8') as file_1:
    x = 0
    for line in file_1:
        x+=1
    lines.append(x)
with open('sorted/1.txt', 'rt', encoding='utf-8') as file_1:
    files_dict[x] = file_1.read()
    names_dict[x] = os.path.basename('sorted/1.txt')

with open('sorted/2.txt', 'rt', encoding='utf-8') as file_2 :
    y = 0
    for line in file_2:
        y += 1
    lines.append(y)
with open('sorted/2.txt', 'rt', encoding='utf-8') as file_2:
    files_dict[y] = file_2.read()
    names_dict[y] = os.path.basename('sorted/2.txt')

with open('sorted/3.txt', 'rt', encoding='utf-8') as file_3:
     w = 0
     for line in file_3:
         w += 1
     lines.append(w)
with open('sorted/3.txt', 'rt', encoding='utf-8') as file_3:
     files_dict[w] = file_3.read()
     names_dict[w] = os.path.basename('sorted/3.txt')

i = len(files_dict)
while i > 0:
    min_lines = files_dict.pop(min(files_dict.keys()))
    min_names = names_dict.pop(min(names_dict.keys()))
    files.append(min_lines)
    names.append(min_names)
    i -= 1

lines.sort()

with open('sorted/4.txt', 'w', encoding='utf-8') as file_4:
    index = 0
    while index <= 2:
        file_4.write(f'{str(names[index])}\n')
        file_4.write(f'{str(lines[index])}\n')
        file_4.write(f'{str(files[index])}\n')
        index +=1







