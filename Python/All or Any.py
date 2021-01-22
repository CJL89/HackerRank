n = '10'
m = '1 2 3 4 5 6 7 8 9 10'.split()

print(all([i > 0 for i in list(map(int, m))]) and any([i == i[::-1] for i in m]))
