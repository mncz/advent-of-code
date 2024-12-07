# Day 7: Bridge Repair - Part Two

from itertools import product

eqs, ans = {}, 0

with open('input.txt') as file:
    for l in file.readlines():
        r, n = l.split(':')
        eqs[int(r)] = [int(i) for i in n[1:-1].split(' ')]

for e in eqs:
    for c in product('*+|', repeat=len(eqs[e])):
        t = eqs[e][0]

        for i in range(1, len(eqs[e])):
            if c[i - 1] == '+':
                t += eqs[e][i]
            elif c[i - 1] == '*':
                t *= eqs[e][i]
            else:
                t = int(f'{t}{eqs[e][i]}')

        if e == t:
            ans += e
            break

print(ans) #
