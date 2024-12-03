# Day 3: Mull It Over - Part Two

import re

do, ans = True, 0

with open('input.txt') as file:
    muls = re.findall(r'mul\([\d]+\,[\d]+\)|do\(\)|don\'t\(\)', file.read())

for m in muls:
    if m == 'do()':
        do = True
    elif m == 'don\'t()':
        do = False
    else:
        if do:
            a, b = re.findall(r'[\d]+', m)
            ans += int(a) * int(b)

print(ans) #118173507
