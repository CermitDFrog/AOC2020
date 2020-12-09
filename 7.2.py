#!python3
from helpers import iter_input

"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags."

input_data = {}
for item in iter_input(7):
    key, rules = item.split("s contain ")
    input_data[key] = {}
    if "no other bags" not in rules:
        for rule in rules.split(', '):
            rule = rule.replace('bags', 'bag').replace('.', '')
            num = rule.split()[0]
            bag = " ".join(rule.split()[1:])
            input_data[key][bag] = num


def solveSevenTwo():
    containers = ["shiny gold bag"]

    def getContainers():
        global containers
        for bagtype in containers:
            for bag, number in input_data[bagtype].items():
                for x in range(int(number)):
                    containers.append(bag)

    getContainers()
    containers.pop(0)
    return len(containers)


print(solveSevenTwo())
