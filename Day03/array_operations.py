import numpy as np

# Problem 1: Scalar & Element-wise Math

matrix = np.arange(1, 7).reshape(2, 3)

print("Original Matrix:")
print(matrix)

multiplied_matrix = matrix * 5

print("\nMatrix after multiplying by 5:")
print(multiplied_matrix)

ones_matrix = np.ones((2, 3), dtype=int)

final_matrix = multiplied_matrix + ones_matrix

print("\nFinal Matrix:")
print(final_matrix)

# Problem 2: Statistical Aggregations

print("\nGlobal Maximum:")
print(np.max(final_matrix))

print("\nSum of Each Column:")
print(np.sum(final_matrix, axis=0))

print("\nMean of Each Row:")
print(np.mean(final_matrix, axis=1))

# Problem 3: Boolean Filtering

random_array = np.random.randint(10, 51, size=10)

print("\nRandom Array:")
print(random_array)

filtered_array = random_array[random_array > 30]

print("\nValues Greater Than 30:")
print(filtered_array)