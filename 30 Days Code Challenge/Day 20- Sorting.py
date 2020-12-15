from collections import deque

n = 3
a = [3,2,1]
b = [1,2,3]

swaps = 0
a_sorted = sorted(a)

while a_sorted != a:
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swaps += 1
            
print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
