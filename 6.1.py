#!python
from helpers import iter_input, iter_group
from string import ascii_lowercase

def countQuestions(groupdata):
    count = 0
    for letter in ascii_lowercase:
        if letter in groupdata:
            count += 1
    return count

groupcounts = []
for group in iter_group('6'):
    print(group)
    groupcounts.append(countQuestions(group))
print(sum(groupcounts))