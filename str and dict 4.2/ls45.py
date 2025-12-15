books = {
   "Саймон Сингх": "Книга шифров",
   "Брюс Шнайер": "Практическая криптография",
   "Нил Стивенсон": "Криптономикон",
   "Дэвид Кан": "Взломщики кодов",
   "Альбрехт Бойтельспахер": "Криптология",
}

print('-')
print('Книги:')
for book in books.values():
    print(book)

print('-')  
print('Авторы:')
for author in books.keys():
    print(author)

print('-')
print('Библиотека:')
for author_, book_ in books.items():
    print(f'{author_} - {book_}')