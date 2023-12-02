# Day 2: Rock Paper Scissors - Part One

file = open('input.txt', 'r')
lines = file.readlines()
shape = { 'X': 1, 'Y': 2, 'Z': 3 }
win = { 'A': 'Y', 'B': 'Z', 'C': 'X' }
draw = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
ans = 0

for l in lines:
    l = l.strip().split(' ')
    out = shape[l[1]]

    if win[l[0]] == l[1]:
        out += 6
    elif draw[l[0]] == l[1]:
        out += 3

    ans += out

print(ans) #11841