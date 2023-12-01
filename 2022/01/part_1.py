# Day 1: Calorie Counting - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0
cal = 0

for l in lines:
    if l == '\n':
        ans = max(cal, ans)
        cal = 0
        continue

    cal += int(l)

print(ans) #65912