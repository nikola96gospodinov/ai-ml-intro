import numpy as np


# Array creation

# 1. A 1D array of numbers from 0 to 9
print(np.array(range(0, 10)))

# 2. A 3x3 matrix of zeros
print(np.zeros((3, 3)))

# 3. A 1D array with 5 evenly spaced values between 0 and 1
print(np.linspace(0, 1, 5))

# 4. A 4x4 identity matrix
print(np.identity(4))

# 5. A 2x3 array of random numbers between 0 and 1
print(np.random.rand(2, 3))

# Array properties
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 1. What is its shape?
print(arr.shape)

# 2. How many dimensions does it have?
print(arr.ndim)

# 3. What is the total number of elements?
print(arr.size)

# 4. What is its data type?
print(arr.dtype)

# 5. Create a flattened 1D version of this array
print(arr.flatten())

# Indexing and slicing

# 1. Extract the element at position (1, 2)
print(arr[0, 1])

# 2. Extract the second row
print(arr[1])

# 3. Extract the third column
print(arr[:, 2])

# 4. Extract the 2x2 subarray in the bottom right corner
# This means to get the 2x2 section from the bottom-right of the array
# For our array with shape (3, 4), this would be the elements at positions:
# (1,2), (1,3), (2,2), (2,3)
print(arr[1:3, 2:4])  # Rows 1-2 (second and third rows), columns 2-3 (third and fourth columns)

# 5. Create a new array containing only elements greater than 5
mask = arr > 5
print(arr[mask])

# Array operations
a = np.array([11, 31, 8])
b = np.array([-4, 4, 54])

# 1. Calculate a + b, a - b, a b, and a / b
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 2. Calculate the square root of each element in a
print(np.sqrt(a))

# 3. Calculate the mean, sum, min, and max of b
print(np.mean(b))
print(np.sum(b))
print(np.min(b))
print(np.max(b))

# 4. Calculate the dot product of a and b
# The dot product is a mathematical operation that takes two vectors and returns a scalar value.
# It's calculated by multiplying corresponding elements and then summing the results.
# For example, the dot product of [a1, a2, a3] and [b1, b2, b3] is (a1*b1 + a2*b2 + a3*b3).
# In NumPy, we can use the np.dot() function or the @ operator to calculate the dot product.
print(np.dot(a, b))

# Broadcasting

# 1. Create a 3x4 array of random integers between 1 and 10
random_array = np.random.randint(1, 11, size=(3, 4))

# 2. Add 5 to every element in the array
random_array + 5

# 3. Multiply each row by the vector [1, 2, 3, 4]
random_array + np.array([1, 2, 3, 4])

# 4. Subtract the mean of each column from the respective column
column_means = np.mean(random_array, axis=0)
centered_array = random_array - column_means
print(centered_array)

# 5. Divide each column by its standard deviation to normalize the data
# Normalizing data means transforming it to have a standard deviation of 1.
# This is useful for machine learning algorithms that are sensitive to the scale of the data.
# We first calculate the standard deviation of each column using np.std(array, axis=0),
# then divide each column by its standard deviation.
column_stds = np.std(random_array, axis=0)
normalized_array = random_array / column_stds
print(normalized_array)