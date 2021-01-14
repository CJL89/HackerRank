A = list(map(int, '1 2 3 5 6 0'.split()))
B = list(map(int,'9 8 5 6 3 2 1 4 7'.split()))

print(all(x in B for x in A))
