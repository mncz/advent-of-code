# Day 5: Supply Stacks - Part Two

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
    a = []

    for i in range(m):
        a.append(s[f-1].pop(0))
    
    s[t-1] = a + s[t-1]

print(''.join([s[i][0] for i in range(len(s))])) #CWMTGHBDW
