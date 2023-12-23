# Day 2: Dive! - Part One

file = open('input.txt', 'r')
lines = file.readlines()
d = {
    'forward': (0, 1),
    'down': (1, 1),
    'up': (1, -1)
}
p = [0, 0]

for l in lines:
    m, u = l.split(' ')
    u = int(u)
    i, n = d[m][0], u * d[m][1]
    p[i] += n

print(p[0] * p[1]) # 2070300
