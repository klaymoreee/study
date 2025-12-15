def hours_to_days(hours, day = 24):
  lenght = hours // day
  return lenght


# не изменяйте код дальше, это проверка
values = [int(x) for x in input().split(" ")]
print(hours_to_days(*values))