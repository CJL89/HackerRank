total_n, total_m = '5', '5'
n = '1 2 3 4 5'
A = '1 3 5 7 9'
B = '2 4 6 8 10'

n = n.split()
A = set(A.split())
B = set(B.split())
counter = 0

for i in A:
    if i in n:
        counter += 1

for ii in B:
    if ii in n:
        counter -= 1

print(counter)

# Faster output:
counter = sum([(i in A) - (i in B) for i in n])
print(counter)
