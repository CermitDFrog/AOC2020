#!python
from helpers import iter_input

def validate(passline):
    rawreq, password = passline.split(':')
    password.strip()
    reqrange, reqletter = rawreq.split()
    reqmin, reqmax = reqrange.split("-")
    if int(reqmin) <= password.count(reqletter) <= int(reqmax):
        return True
    else:
        return False


count = 0
for line in iter_input(2):
    if validate(line):
        count += 1
print(count)
