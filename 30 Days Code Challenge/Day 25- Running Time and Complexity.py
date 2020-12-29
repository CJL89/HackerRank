n = 3
nn = 7

for _ in range(n):
    # nn = int(input())
    if nn == 1 or (nn % 2 == 0 and nn > 2):
        print('Not prime')
    else:
        for ii in range(3, int(nn ** (1/2)) + 1, 2):
            if nn % ii == 0:
                print('Not prime')
                break
        else:
            print('Prime')
