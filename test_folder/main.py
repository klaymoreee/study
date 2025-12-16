from package.module import get_question_data
from random import shuffle

class Question():
    
    def __init__(self, question_txt, question_difficult, correct_answer, user_answer = None):
        self.question_txt = question_txt
        self.question_difficult = int(question_difficult)
        self.correct_answer = correct_answer
        self.f_t_question = False
        self.user_answer = user_answer
        self.cost_scores = 0
        
    def get_points(self):
        return self.question_difficult * 10
    
    def is_correct(self):
        if self.user_answer == self.correct_answer:
            self.f_t_question = True
            return True
        else:
            self.f_t_question = False
            return False
    
    def build_question(self):
        return f'Вопрос: {self.question_txt}\nСложность {self.question_difficult}/5'
    
    def build_feedback(self):
        if self.f_t_question == True:
            self.cost_scores += self.question_difficult * 10
            return f'Ответ верный, получено {self.cost_scores} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.correct_answer}'

def fill_questions():
    questions = []
    for question in get_question_data():
        questions.append(Question(question['q'], question['d'], question['a']))
    return questions

def score_counter():
    scores = 0
    asnswers_amount = 0
    for question in questions:
        if question.is_correct() == True:
            scores += question.get_points()
            asnswers_amount += 1
    return f'Вот и всё!\nОтвечено {asnswers_amount} вопроса из {len(questions)}\nНабрано баллов: {scores}'

def game_process():
    print('Игра начинается!')
    shuffle(questions)
    for question in questions:
        print(question.build_question())
        question.user_answer = input()
        question.is_correct()
        print(question.build_feedback())
    return print(score_counter())

questions = fill_questions()
game_process()
print('lol')