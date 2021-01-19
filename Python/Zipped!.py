total_students, n = map(int, input().split())
students = []

for i in range(n):
    students.append(list(map(float, input().split())))

students = list(zip(*students))

for x in students:
    print(sum(x)/n)
