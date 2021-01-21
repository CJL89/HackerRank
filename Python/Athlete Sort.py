arr = [['10 2 5'],
['7 1 0'],
['9 9 9'],
['1 23 12'],
['6 5 9']]
k = 1

arr.sort(key=lambda x:x[k])

for i in arr:
    print(*i)
