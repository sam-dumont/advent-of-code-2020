import os
import re
import math
from collections import Counter


def shared_chars(s1, s2):
    return sum((Counter(s1) & Counter(s2)).values())


answers = []
answers2 = []

print(os.getcwd())

with open("./input6.txt") as file:
    localanswer = ""
    for answer in file:
        answer = answer.strip()
        if answer == "":
            answers.append(localanswer)
            localanswer = ""
        else:
            for i in answer:
                if not i in localanswer:
                    localanswer = localanswer + i
    answers.append(localanswer)

count = 0
for a in answers:
    count = count + len(a)

print(count)


with open("./input6.txt") as file:
    localanswer = []
    for answer in file:
        answer = ''.join(sorted(answer.strip()))
        if answer == "":
            answers2.append(localanswer)
            localanswer = []
        else:
            localanswer.append(answer)
    answers2.append(localanswer)

res = []

for a in answers2:

    a = sorted(a, key=len, reverse=True)

    letters = ""
    indexloop = 1
    indexstr = 0

    if len(a) == 1:
        letters = a[0]

    while indexstr < len(a[0]):
        indexloop = 1
        letter = a[0][indexstr]
        while indexloop < len(a):
            if not letter in a[indexloop]:
                letter = ""
            indexloop = indexloop + 1

        if not letter in letters:
            letters = letters + letter

        indexstr = indexstr + 1

    res.append(letters)

print(res)

count = 0
for i in res:
    count = count + len(i)

print(count)
