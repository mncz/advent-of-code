# Day 10: Pipe Maze - Part One

file = open('input.txt', 'r')
lines = file.readlines()
lab, start, q = [], None, []
moves = {
    (-1, 0): ['|', '7', 'F'],
    (1, 0): ['|', 'L', 'J'],
    (0, -1): ['-', 'F', 'L'],
    (0, 1): ['-', '7', 'J']
}
ans = 0

for l in lines:
    p = []

    for c in l.strip():
        p.append(c)
    
    lab.append(p)

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 'S':
            lab[i][j] = 0
            start = (i, j)
            q.append(start)
            break

while q:
    x, y = q.pop(0)

    for m in moves:
        if (x + m[0] >= 0 and x + m[0] < len(lab[0]) and 
            y + m[1] >= 0 and y + m[1] < len(lab)):
            if lab[x+m[0]][y+m[1]] in moves[m]:
                lab[x+m[0]][y+m[1]] = lab[x][y] + 1
                ans = max(ans, lab[x+m[0]][y+m[1]])
                q.append((x + m[0], y + m[1]))

print(ans) #7145