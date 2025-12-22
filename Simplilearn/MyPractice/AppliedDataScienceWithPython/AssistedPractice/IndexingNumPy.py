"""
### __Problem Statement:__

1. Create a one-dimensional NumPy array containing at least ten elements
2. Create a 2D NumPy array with a minimum of 3 rows and 4 columns
3. Create a 3D NumPy array with at least 2 matrices, each containing 2 rows and 3 columns
4. Access elements in NumPy arrays and utilize indexing and slicing techniques for efficient data retrieval
5. Access and print various elements from 1D, 2D, and 3D arrays using positive indexing
6. Perform and print some basic arithmetic operations (like addition or  subtraction) using elements accessed from 1D, 2D, and 3D arrays
7. Access and print elements using negative indices in all three arrays
"""
import numpy as np
# 1. Create a one-dimensional NumPy array containing at least ten elements
one_d_array = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
print("One-Dimensional Array:", one_d_array)
# 2. Create a 2D NumPy array with a minimum of 3 rows and 4 columns
two_d_array = np.reshape(one_d_array,(3,4))
print("Two-Dimensional Array:\n", two_d_array)
# 3. Create a 3D NumPy array with at least 2 matrices, each containing 2 rows and 3 columns
three_d_array = np.reshape(one_d_array[:12],(2,2,3))
print("Three-Dimensional Array:\n", three_d_array)
# 4. Access elements in NumPy arrays and utilize indexing and slicing techniques for efficient
# data retrieval
# 5. Access and print various elements from 1D, 2D, and 3D arrays using positive indexing
element_1d = one_d_array[4]
element_2d = two_d_array[1,2]
element_3d = three_d_array[1,0,2]
print("Element from 1D Array at index 4:", element_1d)
print("Element from 2D Array at row 1, column 2:", element_2d)
print("Element from 3D Array at matrix 1, row 0, column 2:", element_3d)
# 6. Perform and print some basic arithmetic operations (like addition or  subtraction) using elements accessed from 1D, 2D, and 3D arrays
sum_1d_2d = element_1d + element_2d
diff_2d_3d = element_2d - element_3d
print("Sum of elements from 1D and 2D arrays:", sum_1d_2d)
print("Difference between elements from 2D and 3D arrays:", diff_2d_3d)
# 7. Access and print elements using negative indices in all three arrays
neg_element_1d = one_d_array[-3]
neg_element_2d = two_d_array[-2,-1]
neg_element_3d = three_d_array[-1,-1,-1]
print("Element from 1D Array at negative index -3:", neg_element_1d)
print("Element from 2D Array at negative indices -2, -1:", neg_element_2d)
print("Element from 3D Array at negative indices -1, -1, -1:", neg_element_3d)