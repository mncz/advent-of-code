# Day 3: Perfectly Spherical Houses in a Vacuum - Part One

file = open('input.txt', 'r')
lines = file.readlines()
x, y = 0, 0
houses = set()
houses.add((x, y))

for c in lines[0]:
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == '^':
        y += 1
    else:
        y -= 1
    
    houses.add((x, y))

print(len(houses)) #2592
