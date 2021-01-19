x, k = '1 4'.split()
P = 'x**3 + x**2 + x + 1'.replace('x', x)

if eval(P) == int(k):
    print(True)
else:
    print(False)
