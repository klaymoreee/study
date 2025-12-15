numbers = input()
note = numbers.split(' ')
count = 0
for x in note:
    count += int(x)
print(count)