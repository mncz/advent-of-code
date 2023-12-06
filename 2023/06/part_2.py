# Day 6: Wait For It - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
t = int(''.join(lines[0].split(':')[1].split()))
d = int(''.join(lines[1].split(':')[1].split()))
a = 0

for i in range(t + 1):
    if i * (t - i) > d:
        a += 1

print(a) #39594072