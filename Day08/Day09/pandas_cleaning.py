import pandas as pd
import numpy as np

# Creating DataFrame with missing values

data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Math_Score": [78, np.nan, 92, 64],
    "Science_Score": [82, 79, np.nan, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# Problem 1

print("\nMissing Values Count:\n")
print(df.isnull().sum())

# Problem 2

# Drop rows where Name is missing
df = df.dropna(subset=["Name"])

# Fill missing Math score with mean
df["Math_Score"] = df["Math_Score"].fillna(
    df["Math_Score"].mean()
)

# Fill missing Science score with mean
df["Science_Score"] = df["Science_Score"].fillna(
    df["Science_Score"].mean()
)

print("\nCleaned DataFrame:\n")
print(df)