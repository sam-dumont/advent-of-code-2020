import os

numbers = []

print(os.getcwd())

with open("./input01.txt") as file:
    for line in file:
        numbers.append(int(line))

numbers.sort()

print("sum of 2\n------")

found = False
index = 0

while not found and index < len(numbers):
    delta = 2020 - numbers[index]
    if delta in numbers:
        print(str(delta) + " + " + str(numbers[index]))
        print(delta * numbers[index])
        found = True
    index = index + 1


found = False
index = 0

print("\n\nsum of 3\n------")

while not found and index < len(numbers):
    for i in range(0, len(numbers)):
        if i != index:
            numberssum = numbers[i] + numbers[index]
            delta = 2020 - numberssum
            if delta in numbers:
                print(str(delta) + " + " +
                      str(numbers[i]) + " + " + str(numbers[index]))
                print(delta * numbers[index] * numbers[i])
                found = True
                break
    index = index + 1
