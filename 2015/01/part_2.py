# Day 1: Not Quite Lisp - Part Two

file = open('input.txt', 'r')
lines = file.readlines()
floor = 0
position = -1

for i in range(len(lines[0])):
    if lines[0][i] == '(':
        floor += 1
    else:
        floor -= 1

        if floor == -1:
            position = i + 1
            break

print(position) #1795