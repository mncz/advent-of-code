# Day 1: Sonar Sweep - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
w = [int(lines[0]), int(lines[1]), int(lines[2])]
prev = sum(w)
ans = 0

for i in range(3, len(lines)):
    w.pop(0)
    w.append(int(lines[i]))
    s = sum(w)

    if s > prev:
        ans += 1
    
    prev = s

print(ans) # 1471
