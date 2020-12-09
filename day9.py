import os
import re
import copy

numbers = []
preambleLength = 25

with open("./input9.txt") as file:
    for number in file:
        numbers.append(int(number))

weakness = 0
i = 0
for number in numbers[preambleLength:]:
    preamble = numbers[i:i+preambleLength]
    for pnumber in preamble:
        if (number - pnumber) in preamble:
            if preamble[preamble.index(number - pnumber)] != pnumber:
                break
    else:
        weakness = number
        break
    i = i + 1

print(weakness)

acc = 0
start = 0
end = 0
i = 0

while acc != weakness:
    while i < len(numbers):
        acc = acc + numbers[i]
        if acc > weakness:
            start = start + 1
            i = start
            acc = 0
            break
        elif acc == weakness:
            end = i
            break
        i = i + 1
    else:
        continue

subset = sorted(numbers[start:end+1])
weakness2 = subset[0] + subset[-1]

print(weakness2)