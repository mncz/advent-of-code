#  Day 2: 1202 Program Alarm - Part Two

file = open('input.txt', 'r')
f = file.readlines()[0].strip().split(',')
t = [int(x) for x in f]

for noun in range(100):
    for verb in range(100):
        m = t.copy()
        m[1], m[2] = noun, verb

        for i in range(0, len(m), 4):
            if m[i] == 99:
                break
            elif m[i] == 1:
                m[m[i+3]] = m[m[i+1]] + m[m[i+2]]
            elif m[i] == 2:
                m[m[i+3]] = m[m[i+1]] * m[m[i+2]]
        
        if m[0] == 19690720:
            print(100 * noun + verb) # 8250
