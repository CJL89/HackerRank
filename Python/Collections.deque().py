from collections import deque

d = deque()

for _ in range(int(input())):
    actions, *n = input().split()
    getattr(d, actions)(*n)

print(*d)
