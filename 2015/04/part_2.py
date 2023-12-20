# Day 4: The Ideal Stocking Stuffer - Part Two

import hashlib

input = 'yzbqklnj'
i = 0

while True:
    s = f'{input}{i}'
    res = hashlib.md5(s.encode())

    if res.hexdigest()[0:6] == '000000':
        break

    i += 1

print(i) # 9962624
