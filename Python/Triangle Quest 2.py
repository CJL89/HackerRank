
for i in range(1,int(5+1)):
    print(*(list(range(1, i)) + list(range(i, 0, -1))), sep='')
