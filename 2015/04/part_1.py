# Day 4: The Ideal Stocking Stuffer - Part One

import hashlib

input = 'yzbqklnj'
i = 0

while True:
    s = f'{input}{i}'
    res = hashlib.md5(s.encode())

    if res.hexdigest()[0:5] == '00000':
        break

    i += 1

print(i) # 282749
