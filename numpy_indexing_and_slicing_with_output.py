# NumPy Indexing and Slicing Notations Guide

import numpy as np

# 1. Basic Slicing
arr = np.array([0, 1, 2, 3, 4])
print("Basic Slicing:", arr[1:4:2])  # Output: [1, 3]

# 2. Ellipsis (...)
arr_3d = np.random.rand(3, 4, 5)
print("Ellipsis Example:", arr_3d[..., 0])  # Selects all rows and columns but only first element in last axis

# 3. Axis-specific Indexing
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Axis-specific Indexing:", arr_2d[:, :3])  # Output: [[1, 2, 3], [5, 6, 7]]

# 4. Advanced Indexing - List/Array Indexing
arr = np.array([10, 20, 30, 40])
print("List Indexing:", arr[[0, 2]])  # Output: [10, 30]

# 4.1 Advanced Indexing - Boolean Masking
mask = np.array([True, False, True, False])
print("Boolean Masking:", arr[mask])  # Output: [10, 30]

# 5. Indexing Multi-dimensional Arrays
arr_2d = np.array([[1, 2], [3, 4]])
print("Multi-dimensional Indexing:", arr_2d[1, 0])  # Output: 3

# 6. Integer Array Indexing
indices = np.array([0, 3])
print("Integer Array Indexing:", arr[indices])  # Output: [10, 40]

# 7. Boolean Array Indexing
print("Boolean Array Indexing:", arr[arr > 20])  # Output: [30, 40]

# 8. Adding a New Axis
arr = np.array([1, 2, 3])
print("Adding New Axis:", arr[:, None])  # Output: [[1], [2], [3]]

# 9. Ellipsis Combined with Slicing
arr_3d = np.random.rand(4, 5, 6)
print("Ellipsis Combined with Slicing:", arr_3d[1, ..., :2])  # Select 2 elements from last axis for row 1

# 10. Step Indexing
arr = np.array([0, 1, 2, 3, 4])
print("Step Indexing:", arr[::2])  # Output: [0, 2, 4]

# 11. Negative Indexing
arr = np.array([10, 20, 30, 40])
print("Negative Indexing:", arr[-1])  # Output: 40
print("Negative Slice:", arr[-2:])  # Output: [30, 40]

# 12. Multi-axis Fancy Indexing
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print("Multi-axis Fancy Indexing:", arr_2d[[0, 2], 1])  # Output: [2, 6]

# 13. Complete Slicing
print("Complete Slicing:", arr_2d[...])  # Output: [[1, 2], [3, 4], [5, 6]]
