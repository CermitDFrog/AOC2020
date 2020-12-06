#!python
from os import path as ospath
from sys import path as syspath


def validate(passline):
    rawreq, password = passline.split(':')
    password.strip()
    reqrange, reqletter = rawreq.split()
    reqmin, reqmax = reqrange.split("-")
    if int(reqmin) <= password.count(reqletter) <= int(reqmax):
        return True
    else:
        return False


with open(ospath.join(syspath[0], 'input'), 'r') as file:
    count = 0
    for line in file:
        if validate(line):
            count += 1
    print(count)
