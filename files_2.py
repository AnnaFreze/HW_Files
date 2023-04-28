import os

files_list = []
files_dict = {}
files_lines = []
for file in os.listdir('sorted'):
    if file.endswith(".txt"):
        files_list.append(file)

for filename in files_list:
   with open(os.path.join("sorted", filename), 'r', encoding = 'utf-8') as f:
       x = 0
       for line in f:
           x += 1
       f.close()
   with open(os.path.join("sorted", filename), 'r', encoding='utf-8') as f:
       files_dict[filename] = [x, f.read()]

sorted_files = {}
sorted_lines = sorted(files_dict.values())

for i in sorted_lines:
    for y in files_dict.keys():
        if files_dict[y] == i:
            sorted_files[y] = files_dict[y]
            break

with open('4.txt', 'w', encoding='utf-8') as file:
    for key, value in sorted_files.items():
        file.write(f'{key}\n {value[0]}\n {value[1]}\n')