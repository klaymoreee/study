locations = {
  "Джакарта": 25, 
  "Норильск" : -34, 
  "Бангкок": 21, 
  "Якутск": -52,
  "Москва": 5,
}

for city, temperature in locations.items():
    if temperature > 10:
        print(city)