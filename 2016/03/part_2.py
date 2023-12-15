# Day 3: Squares With Three Sides - Part Two

def is_triangle(lengths: list[int]) -> int:
    lengths = sorted(lengths)

    if lengths[0] + lengths[1] > lengths[2]:
        return 1
    else:
        return 0

file = open('input.txt', 'r')
lines = file.readlines()
ans = 0

for i in range(0, len(lines), 3):
    a, b, c = [], [], []

    for j in range(0, 3):
        l = [int(x) for x in lines[i+j].split(' ') if x != '']
        print(l)
        a.append(l[0])
        b.append(l[1])
        c.append(l[2])
    
    ans += sum(list(map(is_triangle, [a, b, c])))

print(ans) # 1836