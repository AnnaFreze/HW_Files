import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
heroes_dict = resp.json()

heroes_list = ['Hulk', 'Captain America', 'Thanos']
compare_dict = {}
for person in heroes_dict:
    if person['name'] in heroes_list:
        compare_dict[person['name']] = person['powerstats']['intelligence']

for hero in compare_dict:
    if compare_dict.get(hero) == max(compare_dict.values()):
        print(f'Самый умный супергерой: {hero}')
