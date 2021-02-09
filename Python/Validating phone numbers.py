import re

n = '9587456281'
nn = '1252478965'

for _ in range(1):
    if re.match('[7-9]\d{9}$', nn):
        print('YES')
    else:
        print('NO')
