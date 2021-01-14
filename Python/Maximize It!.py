from itertools import product

n, k = map(int, input().split())
counter = []

for i in range(n):
    count = list(map(int, input().split()[1:]))
    counter.append([x ** 2 for x in count])

print(max(list(sum(x) % k for x in product(*counter))))
