from helpers import iter_input, iter_test

rawdata = []
for line in iter_test():
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
            raise ValueError(f"{checknum} breaks rules.")

validate(5)
