# Day 8: Haunted Wasteland - Part Two

from numpy import lcm

def check_ends(nodes: list[str]) -> bool:
    for n in nodes:
        if n[-1] != 'Z':
            return True
    
    return False

def find_steps(nodes: list[str]) -> int:
    steps = 0

    while check_ends(nodes):
        for m in moves:
            for i in range(len(nodes)):
                if m == 'L':
                    nodes[i] = s[nodes[i]][0]
                else:
                    nodes[i] = s[nodes[i]][1]
        
            steps += 1

            if not check_ends(nodes):
                break
    
    return steps

file = open('input.txt', 'r')
lines = file.readlines()
moves = lines[0].strip()
s, cs, ans = {}, [], 0

for l in lines[2:]:
    k, m = l.strip().split(' = ')
    left, right = m[1:-1].split(', ')
    s[k] = (left, right)

for c in s:
    if c[-1] == 'A':
        cs.append(c)

print(
    lcm(
        lcm(find_steps(cs[:2]), find_steps(cs[2:4])), 
        find_steps(cs[4:])))

#16563603485021
