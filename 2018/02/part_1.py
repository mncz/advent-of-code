# Day 2: Inventory Management System - Part One

from collections import Counter

file = open('input.txt', 'r')
lines = file.readlines()
twos, threes = 0, 0

for l in lines:
    c = Counter(l)

    if 2 in c.values():
        twos += 1
    
    if 3 in c.values():
        threes += 1

print(twos * threes) # 8892
