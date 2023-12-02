# Day 2: Rock Paper Scissors - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
shape = { 'A': 1, 'B': 2, 'C': 3 }
score = { 'X': 0, 'Y': 3, 'Z': 6 }
win = { 'A': 'B', 'B': 'C', 'C': 'A' }
draw = { 'A': 'A', 'B': 'B', 'C': 'C' }
lose = { 'A': 'C', 'B': 'A', 'C': 'B' }
ans = 0

for l in lines:
    l = l.strip().split(' ')
    out = score[l[1]]

    if out == 6:
        out += shape[win[l[0]]]
    elif out == 3:
        out += shape[draw[l[0]]]
    else:
        out += shape[lose[l[0]]]
    
    ans += out

print(ans) #13022