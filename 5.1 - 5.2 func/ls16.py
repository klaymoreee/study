from math import pi

def get_square(radius):
   square = radius ** 2 * 3.14
   return square

# Не удаляйте код ниже, он нужен для проверки

radius = int(input())
square = get_square(radius)
print(square)