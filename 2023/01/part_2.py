import math

file = open('input.txt', 'r')
lines = file.readlines()
nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
ans = 0

for l in lines:
    # l.replace('one', 'o1e')
    # ...
    # l.replace('nine', 'n9e')

    first_key, first_index = None, math.inf
    last_key, last_index = None, -math.inf

    for k in nums.keys():
        i = l.find(k)
        j = l.rfind(k)

        if i >= 0:
            if i < first_index:
                first_index = i
                first_key = k
        
        if j >= 0:
            if j > last_index:
                last_index = j
                last_key = k
    
    left = nums[first_key] if first_key is not None else None
    right = nums[last_key] if last_key is not None else None
    
    for i in range(len(l)):
        if l[i].isnumeric():
            if i < first_index:
                left = int(l[i])
                break
    
    for i in range(len(l) - 1, -1, -1):
        if l[i].isnumeric():
            if i > last_index:
                right = int(l[i])
                break

    ans += int(f'{left}{right}')
    
print(ans) #53855