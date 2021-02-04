import re

S = 10

for i in range(S):
    pattern1 = re.compile(r'(?<=\s)(\&){2}(?=\s)')
    pattern2 = re.compile(r'(?<=\s)(\|){2}(?=\s)')
    print(pattern1.sub('and', pattern2.sub('or', input())))

for _ in range(S):
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' if m.group(1) == '&&' else 'or'), input()))

x  && &   &x
x&|&&|&| ||x
x| |&&|  &&x
x& &   &| &x
x& &&&&||| x
x&|&  |    x
x &  & |&&&x
x|&|& &    x
x & &|| &||x
x |&|&&|&||x
