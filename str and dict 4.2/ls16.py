word = input()

note = []

for x in word:
    note.append(x)
    
word_end = word[0:2] + (len(note[2:-1]) * '*') + word[-1]

print(word_end)