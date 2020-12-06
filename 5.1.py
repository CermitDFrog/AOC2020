#!python
from helpers import iter_input

boardingIDs = []
for line in iter_input(5):
    row = int(line[:7].replace('F', '0').replace('B','1'), 2)
    col = int(line[7:].replace('L', '0').replace('R','1'), 2)
    boardingIDs.append(row * 8 + col)

print(max(boardingIDs))
