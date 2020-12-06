#!python
from helpers import iter_input

seats = [[0 for x in range(8)] for i in range(128)]
for line in iter_input(5):
    row = int(line[:7].replace('F', '0').replace('B','1'), 2)
    col = int(line[7:].replace('L', '0').replace('R','1'), 2)
    seats[row][col] = 1

first = False
for row, line in enumerate(seats):
    if sum(line) == 7:
        for seat, occupied in enumerate(line):
            if occupied == 0:
                print(row*8+seat)
