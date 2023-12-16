# Day 1: Inverse Captcha - Part One

file = open('input.txt', 'r')
seq = file.readlines()[0][:-1]
ans = 0

for i in range(len(seq) - 1):
    if seq[i] == seq[i+1]:
        ans += int(seq[i])

if seq[-1] == seq[0]:
    ans += int(seq[-1])

print(ans) # 1341