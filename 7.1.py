#!python3
from helpers import iter_test, iter_input

input_data = []
for item in iter_input(7):
    input_data.append(item)

def solveSeven():
    containers = ["shiny gold bag"]
    def getContainers():
        containers
        for bagtype in containers:
            for item in input_data:
                bag, contents = item.split("s contain ")
                if bagtype in contents:
                    if bag not in containers:
                        containers.append(bag)
    getContainers()
    containers.pop(0)
    return len(containers)

print(solveSeven())