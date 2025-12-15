employees = [

 {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False}, 
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},   
]

vaccinated = []
not_vaccinated = []

for vacban in employees:
    if vacban['vaccinated'] == True:
        vaccinated.append(vacban["fio"])
    else:
        not_vaccinated.append(vacban["fio"])
        
print("Вакцинированные:")
for vac in vaccinated:
    print(vac)
print("Остальные:")
for ban in not_vaccinated:
    print(ban)