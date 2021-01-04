from collections import OrderedDict

supermarket = OrderedDict()

n = '''
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30'''

for i in range(int(input())):
    items = input().split(' ')
    item_name = ' '.join(items[:-1])
    net_price = int(items[-1])
    if item_name not in supermarket:
        supermarket[item_name] = net_price
    else:
        supermarket[item_name] += net_price

for k, v in supermarket.items():
    print(k, v)
