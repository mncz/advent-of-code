# Day 2: Inventory Management System - Part Two

import nltk

file = open('input.txt', 'r')
lines = file.readlines()
ans = a = b = ''

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if nltk.edit_distance(lines[i], lines[j]) == 1:
            a, b = lines[i], lines[j]
            break

for i in range(len(a)):
    if a[i] == b[i]:
        ans += a[i]

print(ans) # zihwtxagifpbsnwleydukjmqv
