# Day 2: Password Philosophy - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    r, s = l.split(': ')
    r, c = r.split(' ')
    l, h = [int(x) for x in r.split('-')]
    s = s.strip()
    a = 0

    for k in s:
        if k == c:
            a += 1
    
    if a >= l and a <= h:
        ans += 1

print(ans) # 396
