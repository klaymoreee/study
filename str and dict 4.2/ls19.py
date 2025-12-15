words = ["семь", "семнадцать", "пропуск", "прочее", "печенье" ]

symbols = input()

for x in words:
    if symbols in x:
        print(x)