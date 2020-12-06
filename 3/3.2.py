#!python
from os import path as ospath
from sys import path as syspath


class treemap():

    def __init__(self):
        with open(ospath.join(syspath[0], 'input'), 'r') as file:
            self.fullmap = []
            for line in file:
                self.fullmap.append(line.strip("\n"))
        self.mapWidth = len(self.fullmap[0])
        self.maplen = len(self.fullmap)

    def isTree(self, x, y):
        x = x % self.mapWidth
        return (self.fullmap[y][x] == "#")

    def checkSlpe(self, run, rise):
        count = 0
        x = 0
        y = 0
        while y < self.maplen:
            if self.isTree(x, y):
                count += 1
            x += run
            y += rise
        return count


treemap = treemap()
val1 = treemap.checkSlpe(1, 1)
val2 = treemap.checkSlpe(3, 1)
val3 = treemap.checkSlpe(5, 1)
val4 = treemap.checkSlpe(7, 1)
val5 = treemap.checkSlpe(1, 2)
print(val1*val2*val3*val4*val5)