# Day 7: Camel Cards - Part One

from collections import Counter

file = open('input.txt', 'r')
lines = file.readlines()
s = {
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
r, ans = [], 0

for l in lines:
    c, b = l.split(' ')
    c, b = list(c), int(b)

    for i in range(len(c)):
        if c[i] in s:
            c[i] = s[c[i]]
        else:
            c[i] = int(c[i])

    d = Counter(c)
    v = list(d.values())
    m, t = max(v), None

    if m > 3:
        t = m + 1
    elif m == 3:
        if 2 in v:
            t = 4
        else:
            t = 3
    elif m == 2: 
        if v.count(2) > 1:
            t = 2
        else:
            t = 1
    else:
        t = 0

    r.append((c, t, b))

r = sorted(r, key=lambda x: (x[1], x[0]))

for i in range(len(r)):
    ans += (i + 1) * r[i][-1]

print(ans) #250957639
