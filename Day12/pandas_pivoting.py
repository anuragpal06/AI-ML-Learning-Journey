import pandas as pd

# Creating Student Dataset

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Class": ["A", "A", "B", "B", "A", "B"],
    "Gender": ["Female", "Male", "Male", "Male", "Female", "Male"],
    "Math_Score": [78, 85, 92, 88, 90, 75],
    "Science_Score": [82, 79, 89, 90, 95, 80]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# Problem 1: Multi-Level Grouping

print("\nAverage Scores by Class and Gender:\n")

grouped = df.groupby(["Class", "Gender"])[["Math_Score", "Science_Score"]].mean()

print(grouped)

# Problem 2: Pivot Table

print("\nPivot Table (Maximum Science Score):\n")

pivot = pd.pivot_table(
    df,
    index="Class",
    columns="Gender",
    values="Science_Score",
    aggfunc="max"
)

print(pivot)