
#Create and Print Matrix
A = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]

print(A)

for i in range(len(A)):
    print(A[i])

#Print Diagonal Elements
row = len(A)
column = len(A[0])

for i in range(min(row, column)):
    print(A[i][i])

#Matrix addition
A = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]

B = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for row in result:
    print(row)

#Matrix Multiplication
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(matrix_A)):          # rows of A
    for j in range(len(matrix_B[0])):   # columns of B
        for k in range(len(matrix_B)):  # rows of B
            result[i][j] += matrix_A[i][k] * matrix_B[k][j]

for row in result:
    print(row)