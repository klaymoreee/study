def get_min_sec(sec):
    min = sec // 60
    secs = sec % 60
    time = {}
    time['min'] = min
    time['sec'] = secs
    return time

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)  
print(result)