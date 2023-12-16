# Day 2: Corruption Checksum - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    l = [int(x) for x in l.split('\t')]
    
    for n in l:
        for m in l:
            if n != m and n % m == 0:
                ans += (n // m)

print(ans) # 258
