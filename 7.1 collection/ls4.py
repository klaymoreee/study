fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for sea in fish:
    if sea["water"] == "sea":
        sea_water.append(sea["specie"])
    else:
        fresh_water.append(sea["specie"])


print(f"Морские: {', '.join(sea_water)}")
print(f"Пресноводные: {', '.join(fresh_water)}")
