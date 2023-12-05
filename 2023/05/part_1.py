# Day 5: If You Give A Seed A Fertilizer - Part One

file = open('input.txt', 'r')
lines = file.readlines()
seeds = {}
d, s, ln = None, None, None
cat = 'seed'

for s in lines[0].split(': ')[1].strip().split(' '):
    seeds[s] = (int(s), cat)

for l in lines[2:]:
    if len(l) == 0 or not l[0].isnumeric():
        d, s, ln = 0, 0, 0

        if len(l) > 0:
            cat = l.split(' ')[0].split('-')[-1]

        continue
    else:
        d, s, ln = [int(x) for x in l.split(' ')]

        for k in seeds:
            n, t = seeds[k]

            if n >= s and n < s + ln and t != cat:
                n = d + n - s
                t = cat
            
            seeds[k] = (n, t)

print(min(seeds.values())[0]) #111627841