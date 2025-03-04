import numpy as np
import time

# # Vectorisation is faster than traditional loops

# # Create data
# size = 1_000_000
# data = np.random.rand(size)

# # Python loop approach
# def square_with_loop(data):
#     result = [0] * len(data)
#     for i in range(len(data)):
#         result[i] = data[i] ** 2
#     return result

# # NumPy vectorised approach
# def square_with_numpy(data):
#     return data ** 2

# # Measure performance
# start = time.time()
# result_loop = square_with_loop(data)
# loop_time = time.time() - start

# start = time.time()
# result_numpy = square_with_numpy(data)
# numpy_time = time.time() - start

# print(f"Python loop: {loop_time:.6f} seconds")
# print(f"NumPy vectorised: {numpy_time:.6f} seconds")
# print(f"NumPy is {loop_time/numpy_time:.1f} faster")

# # Computing distances

# # Generate sample data: 1000 points in 50-dimensional space
# n_sample = 1000
# n_features = 50
# X = np.random.rand(n_sample, n_features)

# # Python loop approach
# def distances_with_loops(X):
#     n = X.shape[0]
#     distances = np.zeros((n, n))
    
#     for i in range(n):
#         for j in range(n):
#             # Euclidean distance calculation
#             dist = 0
#             for k in range(X.shape[1]):
#                 dist += (X[i, k] - X[j, k]) ** 2
#             distances[i, j] = np.sqrt(dist)
            
#     return distances

# # NumPy vectorised approach
# def distances_with_numpy(X):
#     # Compute squared Euclidean distance using broadcasting
#     sq_dists = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=2)
#     return np.sqrt(sq_dists)
    
# # Measure with a smaller subset for the slow loop version
# small_X = X[:100]  # First 100 samples to make loop version feasible

# # Time the loop version on small data
# start = time.time()
# loop_distances = distances_with_loops(small_X)
# loop_time = time.time() - start
# print(f"Loop version (100 samples): {loop_time:.3f} seconds")

# # Time the NumPy version on the same small data
# start = time.time()
# numpy_distances_small = distances_with_numpy(small_X)
# numpy_time_small = time.time() - start
# print(f"NumPy version (100 samples): {numpy_time_small:.3f} seconds")
# print(f"NumPy is {loop_time/numpy_time_small:.1f}x faster")

# # Now time NumPy on full data to show scalability
# start = time.time()
# numpy_distances = distances_with_numpy(X)
# numpy_time_full = time.time() - start
# print(f"NumPy version (1000 samples): {numpy_time_full:.3f} seconds")


# Broadcasting

# Column vector (3x1)
col = np.array([[1], [2], [3]])
print("Column shape:", col.shape) # (3, 1)

row = np.array([[10, 20, 30, 40]])
print("Row shape:", row.shape)  # (1, 4)

# Broadcasting creates a 3x4 result
result = col + row
print("Result shape:", result.shape)  # (3, 4)
print("Result:")
print(result)
# [[11 21 31 41]
#  [12 22 32 42]
#  [13 23 33 43]]

# NumPy virtually "stretches" the column vector across columns and the row vector across rows to make a 3x4 grid without actually copying data.