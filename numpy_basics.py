import numpy as np

# 1. Create a NumPy array containing numbers from 1 to 10.
arr = np.arange(1, 11)

print("Original Array:", arr)
# 2. Find sum, mean, maximum and minimum

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
# 3. Reverse the array
reversed_arr = arr[::-1]

print("Reversed Array:", reversed_arr)
# 4. Create a 3×3 matrix

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
# 5. Multiply every element of the array by 2

multiplied_arr = arr * 2

print("Array multiplied by 2:", multiplied_arr)