def has_rrr(word):
    if 'р' in word or 'Р' in word:
        return True
    return False

# Не удаляйте код ниже, он нужен для проверки

word = input()
result = has_rrr(word)
print(result)