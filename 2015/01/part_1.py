# Day 1: Not Quite Lisp - Part One

file = open('input.txt', 'r')
lines = file.readlines()
floor = 0

for c in lines[0]:
    if c == '(':
        floor += 1
    else:
        floor -= 1

print(floor) #74