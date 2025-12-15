def lost_time(*numbers):
  summ = 0
  for x in numbers:
      summ += x
  return summ

# Не удаляйте код ниже, он нужен для проверки

numbers = [int(x) for x in input().split(" ")]
print(lost_time(*numbers))