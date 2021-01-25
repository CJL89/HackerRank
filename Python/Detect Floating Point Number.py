import re

n = '4'
m = '4.0O0'
mm = '-1.00'
mmm = '+4.54'
mmmm = 'SomeRandomStuff'

for i in range(int(n)):
    num = m
    if re.match('[+-]?([0-9]+)?\.[0-9]+$', num):
        print(True)
    else:
        print(False)
