import pandas as pd

# Load the CSV file
df = pd.read_csv('bbc_data.csv')

# Print the first few rows of the DataFrame
print("First few rows of the data:")
print(df.head())

# Print summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

# Identify missing values
print("\nMissing values:")
print(df.isnull().sum())

# Print data types
print("\nData types:")
print(df.dtypes)
