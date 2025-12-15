code = "Echo Sierra Charlie Alfa Papa Echo"
new_str = ''
note = code.split(" ")
for x in note:
    new_str += x[0]
print(new_str)