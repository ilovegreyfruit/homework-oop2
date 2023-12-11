with open('recipes.txt', encoding='utf-8') as f:
    data = f.read()
recipes_data = data.split('\n\n')

cook_book = {}

for recipe_data in recipes_data:
    recipe_lines = recipe_data.split('\n')
    recipe_name = recipe_lines[0]
    ingredient_count = int(recipe_lines[1])
    ingredients = []

    for i in range(2, 2 + ingredient_count):
        ingredient_info = recipe_lines[i].split(' | ')
        ingredient_name = ingredient_info[0]
        quantity = int(ingredient_info[1])
        measure = ingredient_info[2]
        ingredient = {'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure}
        ingredients.append(ingredient)

        cook_book[recipe_name] = ingredients
        
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure' : measure, 'quantity' : quantity}
    return shop_list
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)