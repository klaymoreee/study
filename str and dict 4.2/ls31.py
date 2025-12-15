students = {
  "Алиса": 70, 
  "Эльдар" : 20 , 
  "Агата": 40, 
  "Ярослав": 84,
}

user_input = input()

if 0 <= students[user_input] <= 60:
    print(f'{students[user_input]} баллов, оценка C')
elif 61 <= students[user_input] <= 80:
    print(f'{students[user_input]} баллов, оценка B')
elif students[user_input] >= 81:
    print(f'{students[user_input]} баллов, оценка A')