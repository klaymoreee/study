numbers = {
  1: "one",
  2: "two",
  3: "three",
}

numbers[4] = 'four'
numbers[5] = 'five'
numbers[6] = 'six'
numbers[7] = 'seven'
numbers[8] = 'eight'
numbers[9] = 'nine'

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in numbers]))
print("_".join(numbers.values()))