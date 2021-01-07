from itertools import groupby

n = '1222311'
S = ()

for k, c in groupby(n):
    S = len(list(c)), int(k)
    print(S, end=' ')
