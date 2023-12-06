# Day 3: Rucksack Reorganization - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
ch, ans = [], 0

for i in range(0, len(lines), 3):
    p = []

    for c in lines[i]:
        if c in lines[i+1]:
            p.append(c)
    
    for c in p:
        if c in lines[i+2]:
            ch.append(c)
            break

for c in ch:
    o = ord(c)

    if o > 96 and o < 123:
        ans += o - 96
    else:
        ans += o - 38

print(ans) #2838