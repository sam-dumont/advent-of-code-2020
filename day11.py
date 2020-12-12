import os
import re
import copy
import functools

origin = []
seats = []
seatsNew = []

with open("./input11.txt") as file:
    for row in file:
        seatrow = []
        for place in row.strip():
            seatrow.append(place)
        seats.append(seatrow)

seatsNew = copy.deepcopy(seats)
origin = copy.deepcopy(seats)


def getAdjacentSeats(seats, i, j):
    adjacent = []
    for k in range(i-1, i+2):
        if k >= 0 and k < len(seats):
            for l in range(j-1, j+2):
                if l >= 0 and l < len(seats[k]):
                    if k != i or l != j:
                        adjacent.append(seats[k][l])

    return adjacent


def getFirstSeats(seats, i, j):
    adjacent = []

    # LET'S BE DUMB

    for k in range(i-1, -1, -1):
        if seats[k][j] in ["L", "#"]:
            adjacent.append(seats[k][j])
            break

    for k in range(i+1, len(seats)):
        if seats[k][j] in ["L", "#"]:
            adjacent.append(seats[k][j])
            break

    for k in range(j+1, len(seats[i])):
        if seats[i][k] in ["L", "#"]:
            adjacent.append(seats[i][k])
            break

    for k in range(j-1, -1, -1):
        if seats[i][k] in ["L", "#"]:
            adjacent.append(seats[i][k])
            break

    for k, l in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
        if seats[k][l] in ["L", "#"]:
            adjacent.append(seats[k][l])
            break

    for k, l in zip(range(i-1, -1, -1), range(j+1, len(seats[i]))):
        if seats[k][l] in ["L", "#"]:
            adjacent.append(seats[k][l])
            break

    for k, l in zip(range(i+1, len(seats)), range(j-1, -1, -1)):
        if seats[k][l] in ["L", "#"]:
            adjacent.append(seats[k][l])
            break

    for k, l in zip(range(i+1, len(seats)), range(j+1, len(seats[i]))):
        if seats[k][l] in ["L", "#"]:
            adjacent.append(seats[k][l])
            break

    return adjacent


stable = False
while not stable:
    seats = copy.deepcopy(seatsNew)
    i = j = 0
    while i < len(seats):
        while j < len(seats[i]):
            if not seats[i][j] == ".":
                adjacent = getAdjacentSeats(seats, i, j)
                if seats[i][j] == "L":
                    if not "#" in adjacent:
                        seatsNew[i][j] = "#"
                if seats[i][j] == "#":
                    if adjacent.count("#") >= 4:
                        seatsNew[i][j] = "L"
            j = j + 1
        j = 0
        i = i + 1

    if seatsNew == seats:
        stable = True

print(sum(x.count('#') for x in seats))

seats = copy.deepcopy(origin)
seatsNew = copy.deepcopy(origin)

stable = False
while not stable:
    seats = copy.deepcopy(seatsNew)
    i = j = 0
    while i < len(seats):
        while j < len(seats[i]):
            if seats[i][j] != ".":
                firstSeats = getFirstSeats(seats, i, j)
                if seats[i][j] == "L":
                    if not "#" in firstSeats:
                        seatsNew[i][j] = "#"
                if seats[i][j] == "#":
                    if firstSeats.count("#") >= 5:
                        seatsNew[i][j] = "L"
            j = j + 1
        j = 0
        i = i + 1

    for row in seats:
        print("".join(row))
    print(" ")

    if seatsNew == seats:
        stable = True

print(seats)

print(sum(x.count('#') for x in seats))
