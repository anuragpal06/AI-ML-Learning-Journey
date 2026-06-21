import numpy as np

# Student scores
scores = np.array([78, 85, 92, 64, 89, 75, 81, 95])

# Basic statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Standard Deviation:", std_score)

# Highest and lowest values
highest_score = np.max(scores)
lowest_score = np.min(scores)

# Index positions
top_student_index = np.argmax(scores)
lowest_student_index = np.argmin(scores)

print("\nHighest Score:", highest_score)
print("Lowest Score:", lowest_score)

print(
    f"The top student is at Index {top_student_index} "
    f"with a score of {highest_score}."
)

print(
    f"The lowest scoring student is at Index {lowest_student_index} "
    f"with a score of {lowest_score}."
)