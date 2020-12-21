import os
import re
import math
import functools

operations = {}

value = 0

mask1 = 0
mask0 = 0
mask = ""


def maskbits(number,mask0,mask1):
    masked = number | mask0
    masked = masked & mask1
    return int(masked)


with open("./input14.txt") as file:
    rmask = r'mask = ([X01]{36})'

    roperation = r'mem\[(\d+)\] = (\d+)'

    for line in file:
        if re.match(rmask,line):
            mask = re.split(rmask, line)[1]
            mask1 = int(mask.replace("X","1"),2)
            mask0 = int(mask.replace("X","0"),2)

        else:
            op = re.split(roperation,line)
            operations[op[1]] = maskbits(int(op[2]),mask0,mask1)


print(sum(operations.values()))


def processMask(masks,mask0,mask1,bit):
    if bit == 36:
        masks.append((int(mask0,2),int(mask1,2)))
    else:
        if mask[bit] == "X":
            lmask00 = mask0[0:bit] + "0" + mask0[bit+1: ]
            lmask01 = mask0[0:bit] + "1" + mask0[bit+1: ]
            lmask10 = mask1[0:bit] + "0" + mask1[bit+1: ]
            lmask11 = mask1[0:bit] + "1" + mask1[bit+1: ]
            processMask(masks,lmask00,lmask01,bit+1)
            processMask(masks,lmask10,lmask11,bit+1)
        else:
            lmask1 = mask1[0:bit] + "1" + mask1[bit+1: ]
            lmask0 = mask0[0:bit] + "0" + mask0[bit+1: ]
            processMask(masks,lmask0,lmask1,bit+1)


def modifybit(n,  p,  b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def makeFloatingBits(number,index,floatingBits,numbers):
    if index >= len(floatingBits):
        numbers.append(number)
    else:
        makeFloatingBits(modifybit(number,35 - floatingBits[index],0),index + 1,floatingBits,numbers)
        makeFloatingBits(modifybit(number,35 - floatingBits[index],1),index + 1,floatingBits,numbers)


with open("./input14.txt") as file:
    operations2 = {}
    masks = []
    orMask = 0
    rmask = r'mask = ([X01]{36})'
    roperation = r'mem\[(\d+)\] = (\d+)'

    for line in file:
        if re.match(rmask,line):
            mask = re.split(rmask, line)[1]
            masks = []
            orMask = int(mask.replace("X","0"),2)
            floating = [i for i, ltr in enumerate(mask) if ltr == "X"]
        else:
            op = re.split(roperation,line)
            numbers = []
            masked = int(op[1]) | orMask
            makeFloatingBits(masked,0,floating,numbers)
            for number in numbers:
                operations2[number] = int(op[2])

    print(sum(operations2.values()))
