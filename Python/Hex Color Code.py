import re

n = 11
nn = 'color: #FfFdF8; background-color:#aef;'

for i in range(int(n)):
    pattern = re.findall(r'[\s:](#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6}){1,2}[:;,)]', nn)
    if pattern:
        print(*pattern, sep='\n')


# #BED
# {

#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }
