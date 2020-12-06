#!python
from helpers import iter_input

inputdata = [int(line.strip()) for line in iter_input(1)]


def answer():
    for num in inputdata:
        diff = 2020 - num
        if diff in inputdata:
            return diff * num


print(answer())
