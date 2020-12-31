from itertools import permutations

n, nn = input().split(' ')
nn = permutations(sorted(n), int(nn))

for i in nn:
    print(''.join(i))
