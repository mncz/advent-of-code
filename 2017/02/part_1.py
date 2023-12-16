# Day 2: Corruption Checksum - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    l = [int(x) for x in l.split('\t')]
    ans += max(l) - min(l)

print(ans) # 39126
