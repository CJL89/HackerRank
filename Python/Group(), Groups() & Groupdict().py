import re

m = '12345678910111213141516171820212223'

n = re.search(r'([a-z0-9])\1+', m)

try:
    print(n.group(1))
except:
    print(-1)
