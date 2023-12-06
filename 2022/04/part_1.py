# Day 4: Camp Cleanup - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    a, b = l.split(',')
    ax, ay = [int(x) for x in a.split('-')]
    bx, by = [int(x) for x in b.split('-')]

    a = set([i for i in range(ax, ay + 1)])
    b = set([i for i in range(bx, by + 1)])

    if a.issubset(b) or b.issubset(a):
        ans += 1

print(ans) #441
