#!python3
from helpers import iter_test, iter_input

input_data = []
for item in iter_input(7):
    input_data.append(item)

containers = []
def getContainers(bagtype):
    for item in input_data:
        bag, contents = item.split("s contain ")
        if bagtype in contents:
            if bag not in containers:
                containers.append(bag)


getContainers('shiny gold bag')
for bag in containers:
    getContainers(bag)
print(len(containers))
