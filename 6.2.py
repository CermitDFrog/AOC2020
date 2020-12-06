#!python
from helpers import iter_group_test, iter_group
from string import ascii_lowercase

def countQuestions(groupdata):
    count = 0
    for letter in ascii_lowercase:
        for answers in groupdata:
            if letter not in answers:
                break
            else:
                print(answers)
                count += 1
    return count

groupcounts = []
for group in iter_group_test():
    print(group)
    input()
    groupcounts.append(countQuestions(group))
print(sum(groupcounts))
