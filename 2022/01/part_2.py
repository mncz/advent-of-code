# Day 1: Calorie Counting - Part Two

import bisect

file = open('input.txt', 'r')
lines = file.readlines()
cal = 0
bst = [0, 0 , 0]

for l in lines:
    if l == '\n':
        if cal > bst[0]:
            del bst[0]
            bisect.insort(bst, cal)
        cal = 0
        continue

    cal += int(l)

print(sum(bst))