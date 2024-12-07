# Day 6: Guard Gallivant - Part One

m, s, d, ans = [], [0, 0], 0, 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open('input.txt') as file:
    i = 0

    for l in file.read()[:-1].split('\n'):
        j = l.find('^')

        if j >= 0:
            s[0], s[1] = i, j

        m.append(list(l))
        i += 1

while s[0] >= 0 and s[0] < len(m) and s[1] >= 0 and s[1] < len(m[0]):
    if m[s[0]][s[1]] == '.' or m[s[0]][s[1]] == '^':
        m[s[0]][s[1]] = 'X'
        ans += 1
    elif m[s[0]][s[1]] == '#':
        s[0], s[1] = s[0] - dirs[d % 4][0], s[1] - dirs[d % 4][1]
        d += 1
    
    s[0], s[1] = s[0] + dirs[d % 4][0], s[1] + dirs[d % 4][1]

print(ans) #4826
