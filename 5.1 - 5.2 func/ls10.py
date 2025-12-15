def get_period(hour):
    if 0 <= hour <= 6:
        return 'ночь'
    if 7 <= hour <= 11:
        return 'утро'
    if 12 <= hour <= 17:
        return 'день'
    return 'вечер'

# Не удаляйте код ниже, он нужен для проверки

hour = int(input())
time_of_day = get_period(hour)
print(time_of_day)