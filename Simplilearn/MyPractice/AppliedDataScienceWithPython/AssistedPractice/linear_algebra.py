import numpy as np
# 1. Create a two-dimensional NumPy array containing at least 4 elements
two_d_array_1 = np.array([[4, 7], [2, 6]])
print("Two-Dimensional Array_1:\n", two_d_array_1)
# 2. Create another two-dimensional NumPy array with the same shape as the first array
two_d_array_2 = np.array([[5, 8], [3, 4]])
print("Two-Dimensional Array_2:\n", two_d_array_2)
# 3. Addition of two matrices
matrix_addition = np.add(two_d_array_1, two_d_array_2)
print("Matrix Addition:\n", matrix_addition)


def matrix_addition_func(A, B):
    result = np.zeros((A.shape[0], A.shape[1]))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            result[i][j] = A[i][j] + B[i][j]
    return result

print("Enter the rows and columns of first matrixA")
rows_A = int(input("Enter number of rows: "))
cols_A = int(input("Enter number of columns: "))
print("Enter the rows and columns of first matrixB")
rows_B = int(input("Enter number of rows: "))
cols_B = int(input("Enter number of columns: "))
if rows_A != rows_B or cols_A != cols_B:
    print("Error: Matrices must have the same dimensions for addition.")
    exit()
A = []
print("Enter the elements of matrix A row-wise:")
for i in range(rows_A):
    row = list(map(int, input().split()))
    A.append(row)
B = []
print("Enter the elements of matrix B row-wise:")
for i in range(rows_B):
    row = list(map(int, input().split()))
    B.append(row)
A = np.array(A)
B = np.array(B)
print("Matrix Addition Function:\n", matrix_addition_func(A,B))







