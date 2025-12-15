def count_successful(students = [], score = 50):
    count = 0
    for student in students:
        if student >= score:
            count += 1
    return count


print(count_successful(students=[60, 60], score= 60))