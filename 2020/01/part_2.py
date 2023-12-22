# Day 1: Report Repair - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
n, d, ans = [], {}, 0

for l in lines:
    a = int(l)
    n.append(a)
    d[2020 - a] = a

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] in d:
            ans = n[i] * n[j] * d[n[i] + n[j]]
            break

print(ans) # 130933530
