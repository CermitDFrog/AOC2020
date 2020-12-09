from helpers import iter_input, iter_test

rawdata = []
for line in iter_input(9):
    rawdata.append(int(line))

def validate(preambleLen):
    preamble = rawdata[:preambleLen]
    data = rawdata[preambleLen:]

    for checknum in data:
        for prenum in preamble:
            if checknum - prenum in preamble:
                preamble.pop(0)
                preamble.append(checknum)
                break
            else:
                continue
        else:
            return (checknum)


def crack(BadVal, rawdata):
    for index in range(len(rawdata)):
        check = []
        for offset in range(len(rawdata)-index):
            check.append(rawdata[index + offset])
            if sum(check) > BadVal:
                break
            elif sum(check) == BadVal:
                check.sort()
                return check[0] + check[-1]


print(crack(validate(25), rawdata))

