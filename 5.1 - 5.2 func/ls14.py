def get_percent_rounded(fr, sc):
    percent = (fr / sc) * 100
    return f'{round(percent)}%'

# Не удаляйте код ниже, он нужен для проверки

a = int(input())
b = int(input())
print(get_percent_rounded(a, b))