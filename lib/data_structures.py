spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    arr = list()
    for item in spicy_foods:
        arr.append(item["name"])
    return arr


def get_spiciest_foods(spicy_foods):
    arr = list()
    for item in spicy_foods:
        if item['heat_level'] > 5:
            arr.append(item)
    return arr

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        icon =  '🌶'
        calc = icon * item['heat_level']
        print(f"{item['name']} ({(item['cuisine'])}) | Heat Level: {calc}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item['cuisine'] == cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        icon = '🌶'
        calc = icon * item['heat_level']
        if item['heat_level'] > 5:
            print(f"{item['name']} ({item['cuisine']}) | Heat Level: {calc}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for item in spicy_foods:
        total_heat += item['heat_level']
    average_heat = int(total_heat / len(spicy_foods))
    return average_heat
        

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

