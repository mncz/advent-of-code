# Day 5: Supply Stacks - Part One

file = open('input.txt', 'r')
lines = file.readlines()
s = [[] for _ in range(len(lines[0]) // 4)]
y = 0

while lines[y] != '\n':
    j = 0

    for i in range(1, len(lines[y]), 4):
        if lines[y][i].isnumeric():
            break
        elif lines[y][i].isalpha():
            s[j].append(lines[y][i])
        
        j += 1
    
    y += 1

for l in lines[y+1:]:
    n = l.split(' ')
    
    for i in range(3):
        del n[i]
    
    m, f, t = [int(x) for x in n]
    
    for i in range(m):
        x = s[f-1].pop(0)
        s[t-1].insert(0, x)
    
print(''.join([s[i][0] for i in range(len(s))])) #CWMTGHBDW
