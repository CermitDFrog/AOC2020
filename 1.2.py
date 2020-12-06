#!python
from helpers import iter_input

inputdata = [int(line.strip()) for line in iter_input(1)]


def answer():
    for num1 in inputdata:
        diff1 = 2020 - num1
        for num2 in inputdata:
            num3 = diff1 - num2
            if num3 in inputdata:
                return num1 * num2 * num3


print(answer())
