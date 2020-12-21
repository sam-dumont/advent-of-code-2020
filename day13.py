import os
import re
import math
import functools

with open("./input13.txt") as file:
    timestamp = int(file.readline())
    schedule = list(filter("x".__ne__, file.readline().split(",")))
    for i in range(0, len(schedule)):
        schedule[i] = int(schedule[i])

lowest = 100000000000
answer = 0

for bus in schedule:
    nextBus = ((timestamp//bus) + 1)*bus
    if nextBus < lowest:
        lowest = nextBus
        answer = (nextBus - timestamp) * bus

print(answer)

buses = []

with open("./input13.txt") as file:
    timestamp = int(file.readline())
    schedule = file.readline().split(",")
    index = 0
    for i in range(0, len(schedule)):
        if schedule[i] != "x":
            buses.append((index,int(schedule[i])))
        index = index + 1

time, step = 0, 1

for offset, bus in buses:
    while (time + offset) % bus:
        time += step
    step *= bus

print(time)

print(buses)

