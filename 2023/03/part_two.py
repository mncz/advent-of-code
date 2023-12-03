# Day 3: Gear Ratios - Part Two

import math

def is_part(mat, i, j):
    coo = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), 
        (0, 1), (1, -1), (1, 0), (1, 1)
    ]
    m, n = len(mat), len(mat[0])
    
    for x, y in coo:
        if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n:
            if mat[x+i][y+j] == '*':
                return (True, f'{x+i}-{y+j}')
    
    return (False, '')

file = open('input.txt', 'r')
lines = file.readlines()
mat = []
gear = {}
ans = 0
n, part = '', False

for l in lines:
    mat.append(list(l.strip()))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j].isnumeric():
            n = n + mat[i][j]

            if not part:
                (part, star) = is_part(mat, i, j)
                
                if star != '' and star not in gear:
                    gear[star] = []
        else:
            if len(n) and part:
                gear[star].append(int(n))

            n, part = '', False

for k in gear:
    if len(gear[k]) == 2:
        ans += math.prod(gear[k])

print(ans) #84051670