weather = {
"Москва": True, 
"Новосибирск" : True , 
"Екатеринбург": False, 
"Хабаровск": True,
}

location = input()

if weather[location] == True:
    print('Есть осадки')
else: print('Нет осадков')