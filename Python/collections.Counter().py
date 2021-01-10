from collections import Counter

# _ = '10'
size = '2 3 4 5 6 8 7 6 5 18'
sizes = Counter(map(int, size.split()))
n = '1'
total = 0

for i in range(int(n)):
    shoes, price = map(int, '6 55'.split())
    if int(shoes) in sizes and sizes[shoes] > 0:
        total += int(price)
        sizes[shoes] -= 1
    print(price, sizes)
