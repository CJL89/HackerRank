
for i in range(1,int(5+1)):
    print(*(list(range(1, i)) + list(range(i, 0, -1))), sep='')
    # print(sum(map(lambda n: 10**n, range(i)))**2)
