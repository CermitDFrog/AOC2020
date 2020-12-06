#!python
from os import path as ospath
from sys import path as syspath


def validate(passline):
    rawreq, password = passline.split(':')
    reqrange, reqletter = rawreq.split()
    req1, req2 = [int(value) for value in reqrange.split("-")]
    if (password[req1] == reqletter) != (password[req2] == reqletter):
        return True
    else:
        return False


with open(ospath.join(syspath[0], 'input'), 'r') as file:
    count = 0
    lines = 0
    for line in file:
        if validate(line):
            count += 1
    print(count)
