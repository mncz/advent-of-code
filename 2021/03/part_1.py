# Day 3: Binary Diagnostic - Part One

from collections import Counter

file = open('input.txt', 'r')
lines = file.readlines()
gamma = epsilon = ''
b = ['' for _ in range(len(lines[0][:-1]))]

for l in lines:
    for i in range(len(l.strip())):
        b[i] += l[i]

for n in b:
    n = Counter(n).most_common()
    gamma += n[0][0]
    epsilon += n[1][0]

print(int(gamma, 2) * int(epsilon, 2)) # 3912944
