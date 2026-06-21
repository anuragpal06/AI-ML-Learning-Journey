Day 04: Combining, Splitting and Sorting Data

Concatenation and Stacking

NumPy provides functions to combine arrays.

Vertical Stacking

np.vstack((array_A, array_B))

Combines arrays row-wise.

Example:

[[1 2 3]
 [4 5 6]]

Horizontal Stacking

np.hstack((array_A, array_B))

Combines arrays column-wise.

Example:

[1 2 3 4 5 6]

Splitting Arrays

Arrays can be divided into smaller arrays.

Vertical Split

np.vsplit(matrix, 2)

Splits a matrix vertically into equal parts.

Example:

[[1 2]
 [3 4]]
[[5 6]
 [7 8]]

⸻

Sorting Arrays

np.sort(array)

Sorts values in ascending order.

Example:

Before:
[45 12 89 5 23]
After:
[5 12 23 45 89]

Functions Used

* np.array()
* np.vstack()
* np.hstack()
* np.arange()
* reshape()
* np.vsplit()
* np.sort()

Approach Used

Problem 1

Created two arrays and combined them using vertical and horizontal stacking.

Problem 2

Created a 4×2 matrix and split it into two equal matrices using np.vsplit().

Problem 3

Sorted an unsorted array using np.sort().


