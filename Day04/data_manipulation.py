import numpy as np

# Problem 1: Stacking Features

array_A = np.array([1, 2, 3])
array_B = np.array([4, 5, 6])

vertical_stack = np.vstack((array_A, array_B))

horizontal_stack = np.hstack((array_A, array_B))

print("Vertical Stack:")
print(vertical_stack)

print("\nHorizontal Stack:")
print(horizontal_stack)

# Problem 2: Splitting Datasets

matrix = np.arange(1, 9).reshape(4, 2)

print("\nOriginal Matrix:")
print(matrix)

split_matrices = np.vsplit(matrix, 2)

print("\nFirst Split:")
print(split_matrices[0])

print("\nSecond Split:")
print(split_matrices[1])

# Problem 3: Sorting Target Values

unsorted_array = np.array([45, 12, 89, 5, 23])

sorted_array = np.sort(unsorted_array)

print("\nSorted Array:")
print(sorted_array)