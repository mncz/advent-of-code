# Day 3: Gear Ratios - Part One

def is_part(mat, i, j):
    coo = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), 
        (0, 1), (1, -1), (1, 0), (1, 1)
    ]
    m, n = len(mat), len(mat[0])
    
    for x, y in coo:
        if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n:
            if not mat[x+i][y+j].isnumeric() and mat[x+i][y+j] != '.':
                return True
    
    return False

file = open('input.txt', 'r')
lines = file.readlines()
mat = []
ans = 0
n, part = '', False

for l in lines:
    mat.append(list(l.strip()))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j].isnumeric():
            n = n + mat[i][j]

            if not part:
                part = is_part(mat, i, j)
        else:
            if len(n) and part:
                ans += int(n)
                print(n)

            n, part = '', False

print(ans) #532428