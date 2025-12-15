fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

def get_fish(fish_name, note):
    for fishes in note:
        if fishes["specie"] == fish_name:
            return fish_name, fishes["water"]

# Не удаляйте код ниже, он нужен для проверки!

fish_name = input()
fish, water = get_fish(fish_name, fish)
print(fish, water)