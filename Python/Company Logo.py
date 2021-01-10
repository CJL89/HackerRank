from collections import Counter

s = 'qwertyuiopasdfghjklzxcvbnm'
counter = Counter(sorted(s))
ord_counter = counter.most_common(3)

for i in ord_counter:
    if i[1] > 1:
        print(*i)
    else:
        print(*i)
