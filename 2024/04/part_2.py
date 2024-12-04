# Day 4: Ceres Search - Part Two

from typing import List

def search(t: List[str], i: int, j: int) -> int:
    left = ['M', 'M', 'S', 'S']

    for d in directions:
        if t[i + d[0]][j + d[1]] in left:
            left.remove(t[i + d[0]][j + d[1]])
    
    if not left:
        if t[i - 1][j - 1] != t[i + 1][j + 1]:
            return 1
    
    return 0

directions = [
    (-1, -1),       # LT
    (-1, 1),        # RT
    (1, -1),        # LB
    (1, 1)          # RB
]
ans = 0

with open('input.txt') as file:
    txt = file.read().split('\n')
    del txt[-1]     # Linea vuota

n = len(txt)

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if txt[i][j] == 'A':
            ans += search(txt, i, j)

print(ans) #2011
