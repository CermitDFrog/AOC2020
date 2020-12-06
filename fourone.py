from helpers import iter_input, passport


passportraw = ""
count = 0
for line in iter_input(4):
    if line == '\n':
        pport = passport(passportraw)
        if pport.validate():
            count += 1
        passportraw = ''
    else:
        passportraw += f' {line}'
else:
    pport = passport(passportraw)
    if pport.validate():
        count += 1
    passportraw = ''
print(count)
