# Day 1: Trebuchet?! - Part Two

def replace_text(line):
    n = [
        ('one', 'o1e'),
        ('two', 't2o'),
        ('three', 't3e'),
        ('four', '4'),
        ('five', '5e'),
        ('six', '6'),
        ('seven', '7n'),
        ('eight', 'e8t'),
        ('nine', 'n9e')
    ]

    for (x, y) in n:
        line = line.replace(x, y)
    
    return line

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    l = replace_text(l)
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
    
print(ans) #53855