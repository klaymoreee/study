word = input()
len_word = len(word)
if 0 <= len_word <= 3:
    print('короткое слово')
elif 4 <= len_word <= 7:
    print('среднее слово')
elif len_word >= 8:
    print('длинное слово')
