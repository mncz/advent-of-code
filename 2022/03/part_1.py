# Day 3: Rucksack Reorganization - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ch, ans = [], 0

for l in lines:
    h = len(l) // 2
    a, b = l[0:h], l[h:]

    for c in a:
        if c in b:
            ch.append(c)
            break

for c in ch:
    o = ord(c)

    if o > 96 and o < 123:
        ans += o - 96
    else:
        ans += o - 38

print(ans) #7908