# NumPy indexing:
Indexing in NumPy allows you to access or modify specific elements, rows, or columns in an array. By mastering slicing and indexing, you can efficiently manipulate array data for various applications such as machine learning, data processing, and numerical computation.

## Notations Covered in This Guide

### 1. Basic Slicing

> Example:

```Python
arr = np.array([0, 1, 2, 3, 4])
print(arr[1:4:2])  # Output: [1, 3]
```

 **Use Case:** Extract a subarray from a 1D array with step sizes.

### 2. Ellipsis (...)

> Example:
```Python
arr_3d = np.random.rand(3, 4, 5)
print(arr_3d[..., 0])  # Selects all rows and columns but only the first element along the last axis.
```

**Use Case:** Work with multi-dimensional arrays while ignoring certain axes.

### 3. Axis-specific Indexing

> Example:
```Python
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr_2d[:, :3])  # Output: [[1, 2, 3], [5, 6, 7]]
```
**Use Case:** Select specific rows or columns from a 2D array.

### 4. Advanced Indexing

#### 4.1 List or Array Indexing

> Example:
```Python
arr = np.array([10, 20, 30, 40])
print(arr[[0, 2]])  # Output: [10, 30]
```
#### 4.2 Boolean Masking

> Example:
```Python
mask = np.array([True, False, True, False])
print(arr[mask])  # Output: [10, 30]
```
**Use Case:** Extract elements based on specific conditions.

### 5. Multi-dimensional Indexing

> Example:
```Python
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d[1, 0])  # Output: 3
```
**Use Case:** Access individual elements in multi-dimensional arrays.

### 6. Integer Array Indexing

> Example:
```Python
indices = np.array([0, 3])
print(arr[indices])  # Output: [10, 40]
```
**Use Case:** Select multiple specific elements.

### 7. Adding a New Axis

> Example:
```Python
arr = np.array([1, 2, 3])
print(arr[:, None])  # Output: [[1], [2], [3]]
```
**Use Case:** Reshape arrays to add dimensions for broadcasting or compatibility.

### 8. Combining Ellipsis with Slicing

> Example:
```Python
arr_3d = np.random.rand(4, 5, 6)
print(arr_3d[1, ..., :2])  # Selects 2 elements from the last axis for the 2nd row.
```
**Use Case:** Simplify access to slices across complex dimensions.

### 9. Step Indexing

> Example:
```Python
arr = np.array([0, 1, 2, 3, 4])
print(arr[::2])  # Output: [0, 2, 4]
```
**Use Case:** Select elements at regular intervals.

### 10. Negative Indexing

> Example:
```Python
arr = np.array([10, 20, 30, 40])
print(arr[-1])  # Output: 40
print(arr[-2:])  # Output: [30, 40]
```
**Use Case:** Access elements counting from the end of the array.

### 11. Multi-axis Fancy Indexing

> Example:
```Python
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_2d[[0, 2], 1])  # Output: [2, 6]
```
**Use Case:** Select specific rows and columns in multi-dimensional arrays.

### 12. Complete Slicing

> Example:
```Python
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_2d[...])  # Output: [[1, 2], [3, 4], [5, 6]]
```
**Use Case:** Use ... to include all dimensions of an array without explicitly specifying each axis.

## Contributing

If you have additional indexing techniques or examples, feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.