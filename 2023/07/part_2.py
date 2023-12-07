# Day 7: Camel Cards - Part Two

from collections import Counter

file = open('input.txt', 'r')
lines = file.readlines()
s = {
    'J': 1, 'T': 10, 'Q': 11, 'K': 12, 'A': 13
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
    j = d[1] if d[1] else 0
    t = None

    if j:
        del d[1]
        v = list(d.values())

        if not d:
            t = 6
        else:
            m = max(v) if v else 0

            if j > 2: t = j + 1 + m
            elif j == 2:
                if m > 1: t = j + 1 + m
                else: t = j + m
            else:
                if m == 1: t = 1
                elif m > 2: t = j + 1 + m
                else:
                    if v.count(2) > 1: t = 4
                    else: t = 3
    else:
        v = list(d.values())
        m = max(v)
        
        if m > 3: t = m + 1
        elif m == 3:
            if 2 in v: t = 4
            else: t = 3
        elif m == 2: 
            if v.count(2) > 1: t = 2
            else: t = 1
        else: t = 0
    
    r.append((c, t, b))

r = sorted(r, key=lambda x: (x[1], x[0]))

for i in range(len(r)):
    ans += (i + 1) * r[i][-1]

print(ans) #251515496
