# Day 3: Squares With Three Sides - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    l = sorted([int(x) for x in l.split(' ') if x != ''])
    if l[0] + l[1] > l[2]:
        ans += 1

print(ans) # 983