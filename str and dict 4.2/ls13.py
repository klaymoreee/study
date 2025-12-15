sequence = input()

done_sequence = ''

for x in sequence:
    done_sequence += str(bool(int(x)))
    
print(done_sequence)