text = "The quick brown fox jumps over the lazy dog"


def text_length():
    leng = text.split(' ')
    load = ''.join(leng)
    return len(load)
def text_length_full():
    return len(text)

def text_word_count():
    return text.count(' ') + 1

# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())