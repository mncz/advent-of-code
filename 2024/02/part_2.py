# Day 2: Red-Nosed Reports - Part Two

from typing import List

def is_unsafe(r: List[str]) -> bool:
    safe, sign = True, None

    for i in range(len(r) - 1):
        dif = int(r[i]) - int(r[i + 1])

        if ((sign and sign > 0 and dif <= 0) or
            (sign and sign < 0 and dif >= 0)):
            safe = False
            break

        if abs(dif) < 1  or abs(dif) > 3:
            safe = False
            break

        sign = 1 if dif > 0 else -1
    
    return not safe

reports, ans = [], 0

with open('input.txt') as file:
    for l in file:
        reports.append(l.split())
        ans += 1

reports = filter(is_unsafe, reports)

for r in reports:
    stop = False
    ans -= 1

    for i in range(len(r)):
        x = r.copy()
        del x[i]

        if not is_unsafe(x):
            stop = True
            ans += 1
            break

print(ans) #293
