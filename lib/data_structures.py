def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods, heat_level_threshold):
    return [food for food in spicy_foods if food["heat_level"] > heat_level_threshold]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_level_str = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods, heat_level_threshold):
    spiciest_foods = get_spiciest_foods(spicy_foods, heat_level_threshold)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:  # Check if the list is empty
        return 0
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
