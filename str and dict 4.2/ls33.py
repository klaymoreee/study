keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь" ]

word_count = {}

for x in keywords:
    word_count[x] = len(x)
# Не удаляйте код ниже: он нужен для проверки.

print(word_count.get(input()))