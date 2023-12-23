# Day 2: Dive! - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
d = { 'down': 1, 'up': -1 }
p = [0, 0, 0]

for l in lines:
    m, u = l.split(' ')
    u = int(u)

    if m == 'down' or m == 'up':
        p[2] += u * d[m]
    else:
        p[0] += u
        p[1] += p[2] * u

print(p[0] * p[1]) # 2078985210
