# Day 2: Bathroom Security - Part One

file = open('input.txt', 'r')
lines = file.readlines()
t = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
moves = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}
ans = ''

for l in lines:
    l, d = l[:-1], ''
    x = y = 1

    for c in l:
        a = x + moves[c][0]
        b = y + moves[c][1]

        if a >= 0 and a < 3 and b >= 0 and b < 3:
            x, y = a, b
    
    ans += t[x][y]

print(ans) # 69642
