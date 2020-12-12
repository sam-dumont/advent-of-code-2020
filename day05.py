import os
import re
import math

bpasses = []
planeMap = [["" for x in range(8)] for y in range(122)]

print(os.getcwd())

with open("./input05.txt") as file:
    for bpass in file:
        bpasses.append(bpass.strip())


def getLoc(index, column=False):
    lower = 0
    higher = 127
    lowerHalf = "F"
    search = index[0:7]

    if column:
        higher = 7
        lowerHalf = "L"
        search = index[7:]

    for divide in search:
        if divide == lowerHalf:
            higher = higher - math.ceil((higher - lower) / 2)
        else:
            lower = lower + math.ceil((higher - lower) / 2)

    return lower


highest = 0

for bpass in bpasses:

    row = getLoc(bpass)
    column = getLoc(bpass, True)

    planeMap[row][column] = "X"

    mult = (row * 8) + column
    if mult > highest:
        highest = mult

found = False
init = False
i = j = 0

while not found:
    while i < 122 and not found:
        while j < 8 and not found:
            if planeMap[i][j] == "X":
                init = True
            else:
                if init:
                    found = True
            if not found:
                j = j + 1
        if not found:
            j = 0
            i = i + 1


print(highest)
print(((i * 8) + j))
