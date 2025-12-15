text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []

note = text.split(' ')

for x in note:
    if x.isalpha():
        just_words.append(x)

print(' '.join(just_words))