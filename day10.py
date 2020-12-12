import os
import re
import copy
import functools

jolts = [0]
adapters = []

with open("./input10.txt") as file:
    for jolt in file:
        jolts.append(int(jolt))

jolts = sorted(jolts)

highestJoltage = jolts[-1] + 3
jolts.append(highestJoltage)

currentOutlet = 0

adapter3 = 0
adapter1 = 0

while currentOutlet < highestJoltage:
    if (currentOutlet + 1) in jolts:
        currentOutlet = currentOutlet + 1
        adapter1 = adapter1 + 1
    elif (currentOutlet + 3) in jolts:
        currentOutlet = currentOutlet + 3
        adapter3 = adapter3 + 1

print(adapter1 * adapter3)


currentOutlet = 0

adapter3 = 0
adapter1 = 0

totalList = []

global totalCount
totalCount = 0


@functools.lru_cache(1000)
def findNextOutlet(currentJoltage):
    if currentJoltage == highestJoltage:
        return 1

    if currentJoltage not in jolts:
        return 0

    return findNextOutlet(currentJoltage+1) + findNextOutlet(currentJoltage + 2) + findNextOutlet(currentJoltage + 3)


print(findNextOutlet(0))
