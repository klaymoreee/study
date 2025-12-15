def get_grade(points):
    if 0 <= points <= 40:
        return 'Плохо'
    elif 41 <= points <= 60:
        return 'Удовлетворительно'
    elif 61 <= points <= 80:
        return 'Хорошо'
    return 'Отлично' 

# Не удаляйте код ниже, он нужен для проверки

points = int(input())
grade = get_grade(points)
print(grade)