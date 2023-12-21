# Day 1: The Tyranny of the Rocket Equation - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    m = int(l)

    while m > 0:
        f = (m // 3) - 2
        ans = ans + f if f > 0 else ans
        m = f

print(ans) # 5105716
