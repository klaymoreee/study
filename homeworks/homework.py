from random import *

def add_user_data_top(name, score= 0):
    with open('top_list.txt', 'a', encoding="utf-8") as list:
        list.write(f'{name} {score}\n')

def random_word(index_word):
    with open('words.txt', 'rt', encoding= 'utf-8') as note:
        new_list_word = []
        for word in note:
            new_note = []
            word = word.replace('\n', '')
            new_note = list(word)
            shuffle(new_note)
            new_word = ''.join(new_note)
            new_list_word.append(new_word)
        return new_list_word[index_word]

def start_word_set(index_word_set):
    with open('words.txt', 'rt', encoding= 'utf-8') as note:
        set_answers = []
        for word in note:
            word = word.replace('\n', '')
            set_answers.append(word)
        return set_answers[index_word_set]
                        
def len_word_list():
     with open('words.txt', 'rt', encoding= 'utf-8') as note:
         return len(note.readlines())

def statics_games():
    with open('top_list.txt', 'r', encoding='utf-8') as games:
        user_games = []
        for game in games:
            line, _ = game.split(' ')
            user_games.append(line)
        return len(user_games)

def statics_max_score():
        with open('top_list.txt', 'r', encoding='utf-8') as games:
            user_score = []
            for point in games:
                _, score = point.split(' ')
                user_score.append(int(score))
            return max(user_score)
            

score = 0
user_name = input('''Программа: Введите ваше имя
Пользователь:''')


for reload in range(len_word_list()):
    right_word = start_word_set(reload)
    shuffled_word = random_word(reload)
    answer_word = print(f'Программа: Угадайте слово: {shuffled_word}')
    input_word = input('Пользователь: ')
    if input_word == right_word:
        print('Верно! Вы получаете 10 очков!')
        score += 10
    else:
        print(f'Неверно! Верный ответ - {right_word}')

add_user_data_top(user_name, score)
print(f'Всего игр сыграно: {statics_games()}')
print(f'Максимальный рекорд: {statics_max_score()}')