import pandas as pd

file_path = "../dataset/student_stress_dataset.csv"

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())

