# Day 4: Scratchcards - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
d = {}

for i in range(len(lines)):
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

    lines[i] = lines[i].split(':')[1].split(' | ')
    win = lines[i][0].strip().split(' ')
    num = lines[i][1].strip().split(' ')
    m = 0

    for w in win:
        if w != '' and w in num:
            m += 1
    
    if m:
        for j in range(d[i]):
            for k in range(1, m + 1):
                if i + k not in d:
                    d[i+k] = 1
                else:
                    d[i+k] += 1

print(sum(d.values())) #9425061