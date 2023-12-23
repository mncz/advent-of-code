# Day 1: Sonar Sweep - Part One

file = open('input.txt', 'r')
lines = file.readlines()
prev = int(lines[0])
ans = 0

for i in range(1, len(lines)):
    l = int(lines[i])

    if l > prev:
        ans += 1
    
    prev = l

print(ans) # 1448
