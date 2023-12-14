# Day 1: No Time for a Taxicab - Part One

file = open('input.txt', 'r')
lines = file.readlines()[0][:-1]
moves = lines.split(', ')
pos, f, i = (0, 0), 'N', 0
d = {
    'N': { 'R': 'E', 'L': 'W' },
    'E': { 'R': 'S', 'L': 'N' },
    'S': { 'R': 'W', 'L': 'E' },
    'W': { 'R': 'N', 'L': 'S' }
}

for m in moves:
    w, n = m[0], int(m[1:])

    if i % 2 == 0:
        n = -n if d[f][w] == 'W' else n
        pos = (pos[0] + n, pos[1])
    else:
        n = -n if d[f][w] == 'S' else n
        pos = (pos[0], pos[1] + n)

    f = d[f][w]
    i += 1

print(abs(pos[0]) + abs(pos[1])) #287
