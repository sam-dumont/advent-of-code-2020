import os
import re

passports = []

print(os.getcwd())

with open("./input04.txt") as file:
    localpassport = {}
    for passport in file:
        if passport.strip() == "":
            passports.append(localpassport)
            localpassport = {}
        else:
            localpassport.update(
                dict(re.findall(r'(\S+):(".*?"|\S+)', passport)))
    passports.append(localpassport)

print(passports)

print(len(passports))

validpassports = 0

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        validpassports = validpassports + 1

print(validpassports)

validpassports = 0

for passport in passports:
    valid = True

    if "byr" in passport:
        try:
            if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
                valid = False
        except:
            valid = False
    else:
        valid = False

    if "iyr" in passport and valid:
        try:
            if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
                valid = False
        except:
            valid = False
    else:
        valid = False

    if "eyr" in passport and valid:
        try:
            if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
                valid = False
        except:
            valid = False
    else:
        valid = False

    if "hgt" in passport and valid:
        height = re.split(r'(\d+)(in|cm)', passport["hgt"])
        if len(height) == 4:
            if height[2] == "cm" and (int(height[1]) < 150 or int(height[1]) > 193):
                valid = False
            if height[2] == "in" and (int(height[1]) < 59 or int(height[1]) > 76):
                valid = False
        else:
            valid = False
    else:
        valid = False

    if "hcl" in passport and valid:
        if not re.match(r'^#([a-f0-9]{6})$', passport["hcl"]):
            valid = False
    else:
        valid = False

    if "ecl" in passport and valid:
        if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid = False
    else:
        valid = False

    if "pid" in passport and valid:
        if not re.match(r'^(\d{9})$', passport["pid"]):
            valid = False
    else:
        valid = False

    if valid:
        validpassports = validpassports + 1

print(validpassports)
