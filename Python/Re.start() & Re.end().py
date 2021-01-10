import re

S = 'aaadaa'
# S = 'adadad'
k = re.compile('aa')
SS = k.search(S)

if not SS:
    print('(-1, -1)')

while SS:
    print('({}, {})'.format(SS.start(), SS.end() - 1))
    SS = k.search(S, SS.start() + 1)
