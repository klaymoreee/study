def get_rur_kop(value):  
    return value // 100


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_rur_kop(value)
print(result)