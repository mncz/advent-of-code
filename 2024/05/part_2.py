# Day 5: Print Queue - Part Two

from typing import List

def order(update: List[int]) -> List[int]:
    c = [update[0]]

    for u in update[1:]:
        i = 0

        for j in range(len(c)):
            if u in after[c[j]]:
                i = j + 1
        
        for j in range(len(c) - 1, -1, -1):
            if u in before[c[j]]:
                i = j
        
        c.insert(i, u)
    
    return c

before, after, ans = {}, {}, []

with open('input.txt') as file:
    r1, r2 = file.read().split('\n\n')

for r in r1.split('\n'):
    a, b = r.split('|')
    before[b] = [a] if b not in before else before[b] + [a]
    after[a] = [b] if a not in after else after[a] + [b]

for r in r2.split('\n')[:-1]:
    correct = True
    r = r.split(',')
    
    for i in range(len(r)):
        for j in range(i):
            if r[j] in after[r[i]]:
                correct = False
                break
        else:
            for j in range(i + 1, len(r)):
                if r[j] in before[r[i]]:
                    correct = False
                    break
    
    if not correct:
        ans.append(r)

for i in range(len(ans)):
    ans[i] = order(ans[i])

print(sum([int(a[len(a) // 2]) for a in ans])) #5479
