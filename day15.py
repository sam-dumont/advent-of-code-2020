import os
import re
import math
import functools

with open("./input15.txt") as file:
    numbers = [int(x) for x in file.readline().strip().split(",")]


spoken = {0:[100000,0]}
turn = 1
lastSpoken = 0

while turn <= 30000000:
    if turn - 1 < len(numbers):
        spoken[numbers[turn - 1]] = [0,turn]
        lastSpoken = numbers[turn - 1]
    else:
        prevTurn = spoken[lastSpoken][0]
        if prevTurn == 0:
            spoken[0][0] = spoken[0][1]
            spoken[0][1] = turn
            lastSpoken = 0
        else:
            lastSpoken = spoken[lastSpoken][1] - spoken[lastSpoken][0]
            if lastSpoken in spoken.keys():
                spoken[lastSpoken][0] = spoken[lastSpoken][1]
                spoken[lastSpoken][1] = turn
            else:
                spoken[lastSpoken] = [0,turn]
    turn += 1

print(lastSpoken)
