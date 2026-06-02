import pandas as pd

# Dictionary
student = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Rita"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 78, 92, 88, 81]
}

# Create DataFrame
df = pd.DataFrame(student)
print(df)

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Shape
print("Shape of DataFrame:", df.shape)

# Columns
print(df.columns)

# Info
df.info()

# Statistics
print(df.describe())

# Select column
print(df["Name"])

# Multiple columns
print(df[["Name", "Marks"]])

# First row (position-based)
print(df.iloc[0])

# Set custom index
df.index = ["a", "b", "c", "d", "e", "f"]

# First row using label
print(df.loc["a"])

# Correct access after custom index
print(df.loc["a", "Marks"])

# Filter Marks > 80
result = df[df["Marks"] > 80]
print(result)

# Filter Age > 20 AND Marks > 75
result = df[(df["Age"] > 20) & (df["Marks"] > 75)]
print(result)

# Add new column Grade
df["Grade"] = ["A", "A+", "B", "A+", "A", "A"]
print(df)

# Increase Marks by 5
df["Marks"] = df["Marks"] + 5
print(df)

# Update Marks of Ram
df.loc[df["Name"] == "Ram", "Marks"] = 95
print(df)

# Remove Age column
df = df.drop("Age", axis=1)
print(df)

# Remove first row (correct after index change)
df = df.drop("a")
print(df)

# Sort ascending
df = df.sort_values(by="Marks")
print(df)

# Sort descending
df = df.sort_values(by="Marks", ascending=False)
print(df)

# First DataFrame
df1 = pd.DataFrame({
    "Name": ["Ram", "Shyam"],
    "Marks": [85, 90]
})

# Second DataFrame
df2 = pd.DataFrame({
    "Name": ["Hari", "Sita"],
    "Marks": [78, 92]
})

# Concatenate
df = pd.concat([df1, df2], axis=0)
print(df)

# Save to CSV
df.to_csv("students.csv", index=False)

# Read CSV
df = pd.read_csv("students.csv")
print(df)

# Save to Excel
df.to_excel("students.xlsx", index=False)

# Read Excel
df = pd.read_excel("students.xlsx")
print(df)