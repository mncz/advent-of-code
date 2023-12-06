# Day 6: Wait For It - Part One

import math

file = open('input.txt', 'r')
lines = file.readlines()
t = lines[0].split(':')[1].strip().split(' ')
d = lines[1].split(':')[1].strip().split(' ')
r = []

while t.count(''): t.remove('')
while d.count(''): d.remove('')

t = [int(x) for x in t]
d = [int(x) for x in d]

for i in range(len(t)):
    c = 0

    for j in range(t[i] + 1):
        if j * (t[i] - j) > d[i]:
            c += 1
    
    r.append(c)

print(math.prod(r)) #128700