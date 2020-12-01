import re
from collections import Counter

n = 111

binNumber = str(bin(n)[2:])
finder = binNumber.split('0')

print(len(max(finder)))
