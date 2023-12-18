# Day 1: Chronal Calibration - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
i, ans, freq = 0, 0, set()

while ans not in freq:
    freq.add(ans)
    ans += int(lines[i])
    i += 1
    
    if i == len(lines):
        i = 0

print(ans) # 72889