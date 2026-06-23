import pandas as pd

# Creating DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math_Score": [78, 85, 92, 64],
    "Science_Score": [82, 79, 89, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# Problem 1

print("\nName and Science Score:\n")
print(df[["Name", "Science_Score"]])

print("\nThird Student (Charlie):\n")
print(df.iloc[2])

# Problem 2

print("\nStudents scoring above 80 in Math:\n")
print(df[df["Math_Score"] > 80])

print("\nStudents scoring above 75 in both Math and Science:\n")
print(
    df[
        (df["Math_Score"] > 75) &
        (df["Science_Score"] > 75)
    ]
)