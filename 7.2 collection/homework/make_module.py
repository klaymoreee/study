from json import*

def load_students():
    with open('students.json', 'r', encoding= 'utf-8') as file:
        students_list = load(file)
    return students_list

def load_professions():
    with open('professions.json', 'r', encoding= 'utf-8') as note:
        professions_list = load(note)
    return professions_list

def get_student_by_pk(pk):
    for student in load_students():
        if pk == student['pk']:
            return student['full_name'], student['skills']

def get_profession_by_title(title):
    for profession in load_professions():
        if title in profession['title']:
            return profession['skills']
    for profession in load_professions():
        if title not in profession['skills']:
            return 0

def check_fitness(student, profession):
    student_skills = None
    professions_skills = get_profession_by_title(profession)
    for students_data in load_students():
        if student in students_data['full_name']:
            student_skills = students_data['skills']
    set_student_skills = set(student_skills)
    set_professions_note = set(professions_skills)
    has = set_professions_note.intersection(set_student_skills)
    lack = set_professions_note.difference(set_student_skills)
    study_level = 0
    if len(has) != 0:
        study_level = (len(has) / len(professions_skills)) * 100
    skill_ready_check = {'has' :  ', '.join(sorted(has)),
                         'lack' : ', '.join(sorted(lack)),
                         'fit_percent': (f'{int(study_level)}%')}
        
    return skill_ready_check


        
    



