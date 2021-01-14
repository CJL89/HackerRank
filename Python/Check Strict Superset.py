A = set(map(int, '1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78'.split()))
n = '2'
B = set(map(int, '1 2 3 4 5'.split()))
BB = '100 11 12'

print(all([A.issuperset(B) for i in range(int(n))]))
