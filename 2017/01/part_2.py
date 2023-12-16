
# Day 1: Inverse Captcha - Part Two

file = open('input.txt', 'r')
seq = file.readlines()[0][:-1]
m = len(seq)
h, ans = m // 2, 0

for i in range(len(seq)):
    p = i + h if i + h < m else (i + h) % m

    if seq[i] == seq[p]:
        ans += int(seq[i])

print(ans) # 1348
