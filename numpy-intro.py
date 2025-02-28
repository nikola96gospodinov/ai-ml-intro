import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

print(arr2.shape) # (2, 3) - dimensions
print(arr2.ndim) # number of dimensions
print(arr2.size) # 6 - total number of elements
print(arr2.dtype) # int64 - data type

# # Create an array of zeros - Useful: Creating arrays of zeros is useful for initializing arrays that you'll later fill with values.
# zeros = np.zeros((3, 4))
# print(zeros)
# # [[0. 0. 0. 0.]
# #  [0. 0. 0. 0.]
# #  [0. 0. 0. 0.]]

# # Create an array of ones - Useful: Similar to zeros, ones arrays are useful for initialization, especially when you need a starting value of 1.
# ones = np.ones((2, 3))
# # [[1. 1. 1.]
# #  [1. 1. 1.]]

# # Create an array with a range of values
# range_arr = np.arange(0, 10, 2)
# print(range_arr) # [0 2 4 6 8]

# # Create evenly spaced values in a range
# linspace = np.linspace(0, 1, 5) # start, stop, num_points
# print(linspace) # [0.   0.25 0.5  0.75 1.  ]

# # Create an identity matrix
# identity = np.eye(3)
# print(identity)
# # [[1. 0. 0.]
# #  [0. 1. 0.]
# #  [0. 0. 1.]]

# # Random numbers
# random_arr = np.random.rand(2, 3) # Uniform distribution between 0 and 1
# print(random_arr)
# # [[0.19952909 0.87101458 0.39544319]
# #  [0.09303786 0.53449652 0.59070434]] - this will be different on each run

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Get a single element (row, column)
print(arr[0, 0]) # 1 - first element of first row
print(arr[1, 2]) # 7 - third element of second row
print(arr[2, 3]) # 12 - forth element of third row

# Syntax: array[row_start:row_end, col_start:col_end]
print(arr[0:2]) # First two rows
# [[1 2 3 4]
#  [5 6 7 8]]

print(arr[0:2, 0:2]) # First two rows and first two columns
# [[1 2]
#  [5 6]]

print(arr[:, 3]) # All rows but only the last column
# [ 4  8 12]