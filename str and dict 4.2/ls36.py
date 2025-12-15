shopping_list = {
  "Справочник по Python": 2200,
  "Блокнот в клеточку": 800,
  "Набор карандашей": 650
}

new_key = input()
new_value = input()
shopping_list[new_key] = new_value
# Не удаляйте код ниже: он нужен для проверки.

print("_".join(shopping_list))
print("_".join([str(x) for x in shopping_list.values()]))