import pandas as pd

# Creating DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math_Score": [78, 85, 92, 64],
    "Science_Score": [82, 79, 89, 70]
}

df = pd.DataFrame(data)

print("Student DataFrame:\n")
print(df)

print("\nStatistical Summary:\n")
print(df.describe())
