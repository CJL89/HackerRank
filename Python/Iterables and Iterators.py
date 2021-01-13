from itertools import combinations

N = int('9')
s = 'a b c a d b z e o'.split()
K = int('4')

comb = list(combinations(s, K))
counter = []
for i in comb:
    if 'a' in i:
        counter.append(i)

print(len(counter) / len(comb))
