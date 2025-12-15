from make_module import *

while True:
    user_pk_input = int(input('Введите номер студента\nПользователь: '))
    if user_pk_input <= len(load_students()):
        pk_choice = get_student_by_pk(user_pk_input)[0]
        for student in load_students():
            if pk_choice in student['full_name']:
                print(f'Программа: Студент {pk_choice}')
                profession_choiced = input(f'Выберите специальность для оценки студента {pk_choice}\nПользователь: ')
                profession_input = get_profession_by_title(profession_choiced)
                if profession_input != 0:
                    fit_student = check_fitness(pk_choice, profession_choiced)
                    skills_learned = fit_student['has']
                    skills_empty = fit_student['lack']
                    skills_level = fit_student['fit_percent']
                    print(f'Программа: Пригодность {skills_level}\nПрограмма: {pk_choice} знает {skills_learned}\nПрограмма: {pk_choice} не знает {skills_empty}')
                    
                else:
                    print('У нас нет такой специальности')
                    break
        quit()
    else:
        print('У нас нет такого студента')
        break
