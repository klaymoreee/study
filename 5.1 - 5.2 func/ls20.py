def get_distance(liter, consumption = 20):
    need_liters = liter / consumption
    return need_liters
    

# не изменяйте код дальше, это проверка

values = [int(x) for x in input().split(" ")]
print(get_distance(*values))