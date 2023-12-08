# Day 2: I Was Told There Would Be No Math - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for i in lines:
    l, w, h = [int(x) for x in i.split('x')]
    m = [l, w, h]
    m.remove(max(m))
    ans += (m[0] + m[0] + m[1] + m[1]) + (l * w * h)

print(ans) #3812909