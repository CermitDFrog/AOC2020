#!python
from helpers import iter_group_test, iter_group
from string import ascii_lowercase

def countQuestions(groupdata):
    count = 0
    for letter in ascii_lowercase:
        good = True
        for answers in groupdata.splitlines():
            if letter not in answers:
                good = False
                break
        if good:
            count +=1
    return count

groupcounts = []
for group in iter_group(6):
    groupcounts.append(countQuestions(group))
print(sum(groupcounts))
