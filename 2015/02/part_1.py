# Day 2: I Was Told There Would Be No Math - Part One

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for i in lines:
    l, w, h = [int(x) for x in i.split('x')]
    a, b, c = l * w, w * h, h * l
    ans += (2 * a) + (2 * b) + (2 * c) + min(a, b, c)

print(ans) #1598415