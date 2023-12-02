# Day 1: Trebuchet?! - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    left, right = None, None

    for c in l:
        if c.isnumeric():
            left = int(c)
            break
    
    for c in l[::-1]:
        if c.isnumeric():
            right = int(c)
            break
    
    ans += int(f'{left}{right}')

print(ans) #54634