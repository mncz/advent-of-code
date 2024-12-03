# Day 3: Mull It Over - Part One

import re

ans = 0

with open('input.txt') as file:
    muls = re.findall(r'mul\([\d]+\,[\d]+\)', file.read())

for m in muls:
    a, b = re.findall(r'[\d]+', m)
    ans += int(a) * int(b)

print(ans) #184576302
