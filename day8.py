import os
import re
import copy

instructions = []

regex = r'(\w{3}) (\-|\+)(\d+)'

accumulator = 0

with open("./input8.txt") as file:
    for instruction in file:
        elements = re.split(regex, instruction)
        operation = elements[1]
        direction = elements[2]
        value = elements[3]
        instructions.append(
            {"operation": operation, "direction": direction, "value": int(value)})

instructionsRan = []
accumulator = 0
loop = False
index = 0


def processInstruction(instruction, accumulator, index):
    if instruction["operation"] == "jmp":
        if instruction["direction"] == "+":
            index = index + instruction["value"]
        else:
            index = index - instruction["value"]
    else:
        if instruction["operation"] == "acc":
            if instruction["direction"] == "+":
                accumulator = accumulator + instruction["value"]
            else:
                accumulator = accumulator - instruction["value"]
        index = index + 1

    return [accumulator, index]


while not loop:
    instruction = instructions[index]

    if index in instructionsRan:
        loop = True
        break
    else:
        instructionsRan.append(index)

    process = processInstruction(instruction, accumulator, index)
    accumulator = process[0]
    index = process[1]

print(accumulator)

instructionsRan = []
accumulator = 0
loop = False
index = 0


# BRUTEFORCE ALL THE WAY

bigInstructions = []
i = 0

while i < len(instructions):

    bigInstructions.append(copy.deepcopy(instructions))

    if instructions[i]["operation"] == "jmp":
        bigInstructions[i][i]["operation"] = "nop"
    elif instructions[i]["operation"] == "nop":
        bigInstructions[i][i]["operation"] = "jmp"

    i = i + 1

found = False
i = 0

while not found and i < len(bigInstructions):

    instructionsRan = []
    accumulator = 0
    loop = False
    index = 0

    while not loop and index < len(bigInstructions[i]):
        instruction = bigInstructions[i][index]

        if index in instructionsRan:
            loop = True
            break
        else:
            instructionsRan.append(index)

        process = processInstruction(instruction, accumulator, index)
        accumulator = process[0]
        index = process[1]

    if not loop:
        found = True
        print(accumulator)
    i = i + 1
