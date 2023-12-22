# Day 2: Password Philosophy - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    r, s = l.split(': ')
    r, c = r.split(' ')
    l, h = [int(x) for x in r.split('-')]
    s = s.strip()

    if s[l-1] == c and s[h-1] != c or s[l-1] != c and s[h-1] == c:
        ans += 1

print(ans) # 428
