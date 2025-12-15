
words_easy = { 
    "family":"семья", 
    "hand": "рука", 
    "people":"люди", 
    "evening": "вечер",
    "minute":"минута",
}
words_medium = { 
    "believe":"верить", 
    "feel": "чувствовать", 
    "make":"делать", 
    "open": "открывать",
    "think":"думать",   
}
words_hard   = { 
    "rural":"деревенский", 
    "fortune": "удача", 
    "exercise":"упражнение", 
    "suggest": "предлагать",
    "except":"кроме", 
}
rank_answers = {
   0: "Нулевой", 
   1: "Так себе", 
   2: "Можно лучше", 
   3: "Норм", 
   4: "Хорошо", 
   5: "Отлично",
}

right_answers = {}
false_answers = {}

levels = {'Легкий': words_easy, 'Средний' : words_medium, 'Сложный' : words_hard}

start = input('''Программа: Выберите уровень сложности.
Программа: Легкий, средний, сложный.
Пользователь:''')


while True:
    count = 0
    if start not in levels:
        print('Увы, вы не выбрали уровень, попробуйте еще раз: ')
        start = input()
    else:
        print('Программа: Выбран уровень сложности, мы предложим 5 слов, подберите перевод')
        for word, translate in levels[start].items():
            input('''Программа: Нажмите Enter.
Пользователь:''')
            print(f'Программа: {word}, {len(translate)} букв, начинается на {translate[0]}...')
            answer = input('Пользователь: ')
            if answer == translate:
                print(f'Верно, {word} - это {translate}')
                right_answers[word] = 1
            else: 
                print(f'Неверно. {word} - это {translate}.')
                false_answers[word] = 0
            count += 1
    if count == len(levels[start]):
        print('Программа: Правильно отвечены слова:')
        for right in right_answers.keys():
            print(right)
        print('Программа: Неправильно отвечены слова:')
        for false in false_answers.keys():
            print(false)
        score = sum(right_answers.values())
        print(f'''Программа:Ваш ранг: 
{rank_answers[score]}
''')
        break
        
        
            
        