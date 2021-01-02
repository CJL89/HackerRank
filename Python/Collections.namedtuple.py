from collections import namedtuple

n = int(input())
Students = namedtuple('Students', input().split())
total_scores = 0

for i in range(n):
    field1, field2, field3, field4 = input().split()
    xyz = Students(field1, field2, field3, field4)
    total_scores += int(xyz.MARKS)

print('{}'.format(round(total_scores/n, 2)))
