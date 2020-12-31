import math
import cmath
import re

z = '1+2j'
# print(*cmath.polar(complex(z), sep='\n'))

# Using regex:

x, y = map(float, re.findall('[+-]?\d+\.?\d*', z.strip()))
r = math.sqrt((x**2) + (y**2))
yy = cmath.phase(complex(x, y))
print(r, yy, sep='\n')
