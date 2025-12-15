students = {
  1: 25,
  2: 18,
  3: 21,
  4: 18,
  5: 22,
  6: 51
}

del students[2]
del students[3]
del students[5]

# Не удаляйте код ниже: он нужен для проверки.

print("_".join([str(x) for x in students]))
print("_".join([str(x) for x in students.values()]))