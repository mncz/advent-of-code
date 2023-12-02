# Day 2: Cube Conundrum - Part One

file = open('input.txt', 'r')
lines = file.readlines()
reds, greens, blues = 12, 13, 14
ans = 0

for l in lines:
    game = l.split(':')
    id = int(game[0].split(' ')[-1])
    sets = game[1].split(';')
    poss = True

    for s in sets:
        d = { 'red': 0, 'green': 0, 'blue': 0 }
        cubes = s.split(',')

        for c in cubes:
            rev = c.strip().split(' ')
            d[rev[1]] += int(rev[0])

        if d['red'] > reds or d['green'] > greens or d['blue'] > blues:
            poss = False
        
    if poss:
        ans += id

print(ans) #2076