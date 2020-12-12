import os
import re

rows = []

print(os.getcwd())

with open("./input03.txt") as file:
    for row in file:
        rows.append(row.strip())

trees = 0
line = 0
index = 0
end = False

length = 31
height = 323

while not end and line < height:
    if index < length:
        print(f"line {line} index {index}")
        print(rows[line][index])
        if rows[line][index] == "#":
            trees = trees + 1
        index = index + 3
        line = line + 1
    else:
        if line < height:
            index = index % length
        else:
            end = True

print(trees)


trees = 0
line = 0
index = 0
end = False

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
result = 1

length = 31
height = 323

for slope in slopes:
    trees = 0
    line = 0
    index = 0
    end = False

    while not end and line < height:
        if index < length:
            print(f"line {line} index {index}")
            print(rows[line][index])
            if rows[line][index] == "#":
                trees = trees + 1
            index = index + slope[1]
            line = line + slope[0]
        else:
            if line < height:
                index = index % length
            else:
                end = True

    result = result*trees

print(result)
