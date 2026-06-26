import pandas as pd

# Student Data

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math_Score": [78, 85, 92, 88],
    "Science_Score": [82, 79, 89, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# Problem 1

print("\nHigh Achievers:\n")

high_achievers = df[
    (df["Math_Score"] > 85) &
    (df["Science_Score"] > 85)
]

print(high_achievers)

# Problem 2

print("\nAlice and David:\n")

result = df.loc[
    df["Name"].isin(["Alice", "David"]),
    ["Name", "Math_Score"]
]

print(result)