# Day 1: Chronal Calibration - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    ans += int(l)

print(ans) # 518