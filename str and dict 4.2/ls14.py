line = input()

line_spaceless = ' '

for x in line:
    if x not in ['_', ' ']:
        line_spaceless += x
        
# Не удаляйте этот код: он нужен для проверки.

print("".join(line_spaceless))