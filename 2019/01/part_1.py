# Day 1: The Tyranny of the Rocket Equation - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for l in lines:
    ans += (int(l) // 3) - 2

print(ans) # 3405721
