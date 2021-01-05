from itertools import combinations

n = 'HACK 2'
S, k = n.split(' ')

for i in range(1, int(k)+1):
    for ii in combinations(sorted(S), i):
        print(''.join(ii))
