def get_hashtags(text):

    words = text.split(" ")
    hashtags = []
    for word in words:
        if '#' in word:
            word = word.replace('#', "", 1)
            hashtags.append(word)
    return hashtags


# Не удаляйте код ниже, он нужен для проверки    

words = input()
result = get_hashtags(words)
print(result)