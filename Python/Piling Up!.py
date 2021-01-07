from collections import deque

n = '2'
length = '6'
cube = '4 3 2 1 3 4'

for i in range(int(n)):
    _, n = length, deque(map(int, cube.split()))
    ans = True

    for j in range(len(n) - 1):
        if n[0] >= n[1]:
            n.popleft()
        elif n[-1] >= n[-2]:
            n.pop()
        else:
            ans = False
            break

    print('Yes' if ans else 'No')
