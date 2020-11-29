import re
from collections import Counter

n = 6

binNumber = str(bin(n))[2:]
print(binNumber)
finder = re.findall('11+', binNumber)


print(str(finder).split( ))
