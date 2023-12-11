# Day 8: Haunted Wasteland - Part One

file = open('input.txt', 'r')
lines = file.readlines()
moves = lines[0].strip()
s, c, ans = {}, 'AAA', 0

for l in lines[2:]:
    k, m = l.strip().split(' = ')
    left, right = m[1:-1].split(', ')
    s[k] = (left, right)

while c != 'ZZZ':
    for m in moves:
        if m == 'L':
            c = s[c][0]
        else:
            c = s[c][1]
        
        ans += 1

        if c == 'ZZZ':
            break

print(ans) #16897
