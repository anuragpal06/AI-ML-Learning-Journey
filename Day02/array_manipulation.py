import numpy as np

# Problem 1: Inspecting Data

arr = np.arange(10, 22)

print("Original Array:")
print(arr)

print("\nShape:", arr.shape)
print("Size:", arr.size) 
print("Data Type:", arr.dtype)

# Problem 2: Reshaping and Slicing

matrix = arr.reshape(3, 4)

print("\n3x4 Matrix:")
print(matrix)

# First row
first_row = matrix[0]

print("\nFirst Row:")
print(first_row)

# Last two columns
last_two_columns = matrix[:, 2:]

print("\nLast Two Columns:")
print(last_two_columns)

# Problem 3: Flattening Data

flat_array = matrix.flatten()

print("\nFlattened Array:")
print(flat_array)

# Problem 4: Statistical Operations

flat_array = np.random.randint(1, 101, size=12) 
print("\nRandom Array for Statistical Operations:")