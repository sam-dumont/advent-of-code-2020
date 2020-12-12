import os
import re

passwords = []

print(os.getcwd())

with open("./input02.txt") as file:
    for line in file:
        password = re.split(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)', line)
        passwords.append({
            'password': password[4],
            'min': int(password[1]),
            'max': int(password[2]),
            'letter': password[3]
        })

ok_passwords = 0

for password in passwords:
    count = password['password'].count(password['letter'])
    if count >= password['min'] and count <= password['max']:
        ok_passwords = ok_passwords + 1

print(f"number of passwords {ok_passwords}")

ok_passwords = 0

for password in passwords:
    count = password['password'].count(password['letter'])
    if len(password['password']) >= (password['max'] - 1) and len(password['password']) >= (password['min'] - 1):
        firstPos = password['password'][password['min'] - 1]
        secondPos = password['password'][password['max'] - 1]
        letter = password['letter']
        if (firstPos == letter and secondPos != letter) or (firstPos != letter and secondPos == letter):
            ok_passwords = ok_passwords + 1

print(f"number of passwords {ok_passwords}")
