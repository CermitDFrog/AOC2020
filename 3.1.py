#!python
from helpers import iter_input

class treemap():

    def __init__(self):
        self.fullmap = []
        for line in iter_input(3):
            self.fullmap.append(line.strip("\n"))
        self.mapWidth = len(self.fullmap[0])
        self.maplen = len(self.fullmap)

    def isTree(self, x, y):
        x = x % self.mapWidth
        return (self.fullmap[y][x] == "#")


treemap = treemap()
count = 0
x = 0
for y in range(treemap.maplen):
    if treemap.isTree(x, y):
        count += 1
    x += 3

print(count)
