matrix = [[1,1,1,0,0,0,1],
[0,1,0,0,0,0,1],
[1,1,1,0,0,0,2],
[0,0,2,4,4,0,3],
[0,0,0,2,0,0,4],
[0,0,1,2,4,0,5]]

result = []

for i in range(len(matrix)-2):
    for ii in range(len(matrix[0])-2):
        total = sum((matrix[i][ii:ii+3])) + (matrix[i+1][ii+1]) + sum((matrix[i+2][ii:ii+3]))
        result.append(total)
print(result, max(result))
