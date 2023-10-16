from math import trunc

size = int(input("Enter size of square matrix: "))
matrix = []
result = [];

for i in range(size):
    matrix.append(list(input("Enter row: ")))

for k in range(0, trunc((size+1)/2)):
    for i in range(k, size-k-1):
        result.append(matrix[k][i])
    for i in range(k, size-k-1):
        result.append(matrix[i][size-k-1])
    for i in range(size - k - 1, k, -1):
        result.append(matrix[size-k-1][i])
    for i in range(size - k-1, k, -1):
        result.append(matrix[i][k])

print(result)