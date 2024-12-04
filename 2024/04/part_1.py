# Day 4: Ceres Search - Part One

from typing import List

def search(
        t: List[str], 
        d: tuple[int, int], 
        i: int, 
        j: int, 
        left: List[str]) -> int:
    if left:
        i += d[0]
        j += d[1]

        if 0 <= i < len(t) and 0 <= j < len(t):
            x = left.pop()

            if x == t[i][j]:
                return search(t, d, i, j, left)
    else:
        return 1
    
    return 0

directions = [
    (-1, -1),       # LT
    (-1, 0),        # T
    (-1, 1),        # RT
    (0, -1),        # L
    (0, 1),         # R
    (1, -1),        # LB
    (1, 0),         # B
    (1, 1)          # RB
]
ans = 0

with open('input.txt') as file:
    txt = file.read().split('\n')
    del txt[-1]     # Linea vuota

n = len(txt)

for i in range(n):
    for j in range(n):
        if txt[i][j] == 'X':
            for d in directions:
                ans += search(txt, d, i, j, ['S', 'A', 'M'])

print(ans) #2618
