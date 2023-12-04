# Day 4: Scratchcards - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    l = l.split(':')[1].split(' | ')
    win = l[0].strip().split(' ')
    num = l[1].strip().split(' ')
    p = 0

    for w in win:
        if w != '' and w in num:
            p = p + 1 if p == 0 else p * 2
    
    ans += p

print(ans) #28538