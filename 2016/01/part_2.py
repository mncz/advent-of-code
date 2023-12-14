# Day 1: No Time for a Taxicab - Part Two

file = open('input.txt', 'r')
lines = file.readlines()[0][:-1]
moves = lines.split(', ')
pos, f, i, v = (0, 0), 'N', 0, set({(0, 0)})
d = {
    'N': { 'R': 'E', 'L': 'W' },
    'E': { 'R': 'S', 'L': 'N' },
    'S': { 'R': 'W', 'L': 'E' },
    'W': { 'R': 'N', 'L': 'S' }
}
ans = False

for m in moves:
    w, n = m[0], int(m[1:])

    if i % 2 == 0:
        n = -n if d[f][w] == 'W' else n
        s = 1 if n > 0 else -1

        for j in range(s, n + s, s):
            pos = (pos[0] + s, pos[1])

            if pos in v:
                ans = True
                break
            else:
                v.add(pos)
    else:
        n = -n if d[f][w] == 'S' else n
        s = 1 if n > 0 else -1

        for j in range(s, n + s, s):
            pos = (pos[0], pos[1] + s)

            if pos in v:
                ans = True
                break
            else:
                v.add(pos)

    if ans:
        break

    f = d[f][w]
    i += 1

print(abs(pos[0]) + abs(pos[1])) #133
