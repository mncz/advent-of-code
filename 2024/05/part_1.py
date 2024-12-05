# Day 5: Print Queue - Part One

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
    
    if correct:
        ans.append(r)

print(sum([int(a[len(a) // 2]) for a in ans])) #5991
