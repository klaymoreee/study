def get_longest(words):
    print(words)
    note = [len(word) for word in words]
    note_max = max(note)
    for bob in words:
        if len(bob) == note_max:
            return bob

# Не удаляйте код ниже, он нужен для проверки

words = input().split(" ")
result = get_longest(words)
print(result)