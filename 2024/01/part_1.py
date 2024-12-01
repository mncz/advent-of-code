# Day 1: Historian Hysteria - Part One

import bisect

l, r = [], []
d = 0

with open('input.txt') as file:
    for line in file:
        line = ''.join(line.split())
        bisect.insort(l, int(line[:5]))
        bisect.insort(r, int(line[5:]))

for i in range(len(r)):
    d += abs(l[i] - r[i])

print(d) #1388114
