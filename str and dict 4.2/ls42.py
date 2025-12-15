guests = {
  "Алиса": True, 
  "Эльдар" : False, 
  "Агата": False, 
  "Ярослав": True,
}

for x, y in guests.items():
    if y == True:
        print(x)