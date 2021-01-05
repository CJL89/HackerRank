from collections import Counter

n = int(input())
S = [input().strip() for _ in range(n)]
counter = Counter(S)

print(len(set(counter)))

for k, v in counter.items():
    print(v, end=' ')
