import pandas as pd

df = pd.read_csv("students.csv")

print("===== Student Data Analysis System =====")

print("\nDataset Preview:")
print(df.head())

print("\nAverage GPA:")
print(df["GPA"].mean())

print("\nTop Student:")
print(df.loc[df["GPA"].idxmax()])

print("\nStudents with GPA above 3.5:")
print(df[df["GPA"] > 3.5])

print("\nDepartment-wise Student Count:")
print(df["Department"].value_counts())
