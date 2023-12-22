# Day 1: Report Repair - Part One

file = open('input.txt', 'r')
lines = file.readlines()
d = {}

for l in lines:
    a = int(l)
    b = 2020 - a

    if a in d:
        print(a * b) # 888331
        break
    else:
        d[b] = a