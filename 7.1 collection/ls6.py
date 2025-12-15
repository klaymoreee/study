

def local(luck):
    order_converted = []
    for information in luck:
        redo_dict = {"count" : int(information['skolko']),
                    "specie" : (information["poroda"]).replace(information["poroda"][0], information["poroda"][0].upper(), 1),
                    "avg_size" : (information["sred_razmer"] // 10)}     
        order_converted.append(redo_dict)
    return order_converted


order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = local(order)


# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)