import os

with open('py-homework-basic-files/2.4.files/recipes.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name' : ingredient, 'quantity' : int(quantity), 'measure' : measure})
        file.readline()
        cook_book[recipe_name] = ingredients
    print(cook_book)

dishes_list = ['Запеченный картофель', 'Омлет', 'Фахитос']

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingredient_list = []
    item = int

    for dish in dishes:
        ingredient_list += cook_book.get(dish)
        for ingredient in ingredient_list:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list.update({ingredient.get('ingredient_name'): {'measure' : ingredient.get('measure'), 'quantity': int(ingredient.get('quantity')) * person_count}})
            else:
                item = ingredient['quantity']
    if ingredient['ingredient_name'] in shop_list.keys():
       shop_list[ingredient['ingredient_name']]['quantity'] += item * person_count


    return shop_list

print(get_shop_list_by_dishes(dishes_list, 3))



