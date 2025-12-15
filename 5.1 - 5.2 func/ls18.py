def get_discount(summ):
    if summ <= 5000:
        return 1
    elif summ <= 10000:
        return 2
    elif summ <= 20000:
        return 3
    elif summ <= 35000:
        return 4
    elif summ <= 50000:
        return 5
    return 6

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)  
print(result)