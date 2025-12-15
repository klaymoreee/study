year = input()
month = input()
day = input()

birth_date = {'year' : year, 'month' : month, 'day' : day}
print(*birth_date)
# Не удаляйте код ниже: он нужен для проверки.

print(" ".join([x for x in birth_date.keys()]))
print(" ".join([str(x) for x in birth_date.values()]))