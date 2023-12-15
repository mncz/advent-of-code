# Day 2: Bathroom Security - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
t = [
    ['0', '0', '1', '0', '0'], 
    ['0', '2', '3', '4', '0'], 
    ['5', '6', '7', '8', '9'],
    ['0', 'A', 'B', 'C', '0'],    
    ['0', '0', 'D', '0', '0'] 
]
moves = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}
ans, x, y = '', 2, 0

for l in lines:
    l, d = l[:-1], ''

    for c in l:
        a = x + moves[c][0]
        b = y + moves[c][1]

        if a >= 0 and a < 5 and b >= 0 and b < 5 and t[a][b] != '0':
            x, y = a, b
    
    ans += t[x][y]

print(ans) # 8CB23