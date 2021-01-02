n = 1
# nn = '1 0'
nn = '1 $'

for i in range(n):
    try:
        a, b = map(int, nn.split(' '))
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print('Error Code: integer division or modulo by zero')
    except ValueError as ee:
        print('Error Code:', ee)
