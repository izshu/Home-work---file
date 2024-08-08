def read_recipes(file_name):
    cook_book = {}
    with open(file_name, "r") as file:
        lines = file.readlines()

        current_dish = None
    for line in lines:
        line = line.strip()

        if line.isdigit():
            cook_book[current_dish] = []
        elif "|" in line:
            ing_parts = line.split("|")
            ing = {
                "ingredient_name": ing_parts[0].strip(),
                "quantity": int(ing_parts[1].strip()),
                "measure": ing_parts[2].strip(),
            }
            cook_book[current_dish].append(ing)
        else:
            current_dish = line
    return cook_book


filename = "recipe.txt"
cook_book = read_recipes(filename)


def get_shop_list_by_dishes(dishes, person_count):
    x = read_recipes("recipe.txt")
    result = {}
    for dish in dishes:
        for ing_parts in cook_book.get(dish):
            ingredient = ing_parts["ingredient_name"]
            if ingredient in result:
                result[ingredient]["quantity"] += ing_parts["quantity"] * person_count
            else:
                result[ingredient] = {"measure": ing_parts["measure"], "quantity": ing_parts["quantity"] * person_count}
    return result


print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))
