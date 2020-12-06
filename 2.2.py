#!python
from helpers import iter_input


def validate(passline):
    rawreq, password = passline.split(':')
    reqrange, reqletter = rawreq.split()
    req1, req2 = [int(value) for value in reqrange.split("-")]
    if (password[req1] == reqletter) != (password[req2] == reqletter):
        return True
    else:
        return False


count = 0
lines = 0
for line in iter_input(2):
    if validate(line):
        count += 1
print(count)
