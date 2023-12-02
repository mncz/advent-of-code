# Day 2: Cube Conundrum - Part Two

import math

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    game = l.split(':')
    id = int(game[0].split(' ')[-1])
    sets = game[1].split(';')
    d = { 'red': -math.inf, 'green': -math.inf, 'blue': -math.inf }

    for s in sets:
        cubes = s.split(',')

        for c in cubes:
            rev = c.strip().split(' ')
            d[rev[1]] = max(d[rev[1]], int(rev[0]))
    
    ans += math.prod(d.values())

print(ans) #70950