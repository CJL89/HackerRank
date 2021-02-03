import re

n = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
m = 'match a single character not present in the list below'
o = 'abaabaabaabaae'

nn = re.findall(r'(?=([^aeiou\+\-][aeiou]{2,}[^aeiou\+\-]))', m, flags=re.I)

if len(nn) == 0:
    print(-1)
for i in nn:
    print(i[1:-1], sep='\n')
