price = {1 : 30, 2 : 34, 3 : 321, 4 : 12}
price_sum = sum(price.values())

note_pr1 = []
note_pr2 = []
a = {}


for x, v in price.items():
    note_pr1.append(x)
    note_pr2.append(v)  
    if v < 50:
        a[x] = v
print(note_pr1, note_pr2, a)