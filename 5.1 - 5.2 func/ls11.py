def avg(items):
    lost = sum(items) / len(items)
    return lost
# Не удаляйте код ниже, он нужен для проверки

items = [int(x) for x in input().split(" ")]
items_avg = avg(items)
print(items_avg)