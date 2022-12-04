with open('recipes.txt', encoding='utf-8') as f:
    cook_book = []
    for line in f:
        cook_book_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip()
            name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book.append({
            'employees_count': ingredients_count,
            'employees': ingredients
        })
        cook_book_names = {cook_book_name: cook_book}

print(cook_book_names)
print(type(cook_book_names))