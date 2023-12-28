#  Day 2: 1202 Program Alarm - Part One

file = open('input.txt', 'r')
m = file.readlines()[0].strip().split(',')
m = [int(x) for x in m]
m[1], m[2] = 12, 2

for i in range(0, len(m), 4):
    if m[i] == 99:
        break
    elif m[i] == 1:
        m[m[i+3]] = m[m[i+1]] + m[m[i+2]]
    elif m[i] == 2:
        m[m[i+3]] = m[m[i+1]] * m[m[i+2]]

print(m[0]) # 3562672
