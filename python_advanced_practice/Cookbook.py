def cookbook(*stuff):
    group = {}

    for i in range(len(stuff)):
        curr_recipy_name, curr_cuisine, curr_ingredients = stuff[i][0], stuff[i][1], stuff[i][2]
        if curr_cuisine not in group:
            group[curr_cuisine] = (0, [], [])
        count, curr_recipy_list, curr_ingredients_list = group[curr_cuisine]

        count += 1

        curr_recipy_list.append(curr_recipy_name)
        curr_ingredients_list.append(curr_ingredients)

        group[curr_cuisine] = (count,curr_recipy_list, curr_ingredients_list)
    sorted_cookbook = sorted(group.items(), key=lambda x: (-x[1][0], x[0]))
    final_stuff = ""
    for cuisine, (count, recipe_list, ingredient_list) in sorted_cookbook:
        final_stuff += f"{cuisine} cuisine contains {count} recipes:\n"

        sorted_recipes = sorted(zip(recipe_list, ingredient_list))
        for recipe, ingredients in sorted_recipes:
            final_stuff += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return final_stuff







print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
