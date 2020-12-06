#!python
from os import path as ospath
from sys import path as syspath

with open(ospath.join(syspath[0], 'input'), 'r') as file:
    inputdata = [int(line.strip()) for line in file]


def answer():
    for num in inputdata:
        diff = 2020 - num
        if diff in inputdata:
            return diff * num


print(answer())
