n = '5'
cube = lambda x: x ** 3

def fibonacci(n):
    a, b = 0, 1
    for i in range(int(n)):
        yield a
        a, b = b, a + b

print(list(map(cube, fibonacci(n))))
