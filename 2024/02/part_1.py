# Day 2: Red-Nosed Reports - Part One

ans = 0

with open('input.txt') as file:
    for l in file:
        l = l.split()
        safe, sign = True, None

        for i in range(len(l) - 1):
            dif = int(l[i]) - int(l[i + 1])

            if ((sign and sign > 0 and dif <= 0) or
                (sign and sign < 0 and dif >= 0)):
                safe = False
                break

            if abs(dif) < 1  or abs(dif) > 3:
                safe = False
                break

            sign = 1 if dif > 0 else -1
        
        if safe:
            ans += 1

print(ans) #224
