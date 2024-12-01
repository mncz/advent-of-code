# Day 1: Historian Hysteria - Part Two

l, r = [], {}
s = 0

with open('input.txt') as file:
    for line in file:
        line = ''.join(line.split())
        right = int(line[5:])

        l.append(int(line[:5]))

        if right in r:
            r[right] += 1
        else:
            r[right] = 1

for left in l:
    if left in r:
        s += (left * r[left])

print(s) #23529853