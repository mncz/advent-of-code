# Day 3: Perfectly Spherical Houses in a Vacuum - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
c = { 0: [0, 0], 1: [0, 0]}
houses = set()
houses.add((0, 0))

for i in range(len(lines[0])):
    s = i % 2

    if lines[0][i] == '>':
        c[s][0] += 1
    elif lines[0][i] == '<':
        c[s][0] -= 1
    elif lines[0][i] == '^':
        c[s][1] += 1
    else:
        c[s][1] -= 1
    
    houses.add((c[s][0], c[s][1]))

print(len(houses)) #2360
