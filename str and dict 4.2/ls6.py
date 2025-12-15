line = input()

done_line = ''

for x in line:
    if x == '0' or x == '1':
        done_line += x

print(done_line)