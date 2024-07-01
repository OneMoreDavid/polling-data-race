import pandas as pd
import os

# Load the CSV file
try:
    df = pd.read_csv('bbc_data.csv')
    print("Data loaded successfully from bbc_data.csv")
except FileNotFoundError:
    print("Error: bbc_data.csv file not found.")
    exit()

# Check if 'Date' column exists
if 'Date' not in df.columns:
    print("Error: 'Date' column not found in the data")
    print("Available columns:", df.columns)
else:
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Drop rows with missing or invalid dates
    df_cleaned = df.dropna(subset=['Date'])

    # Additional cleaning steps can be added here

    # Save the cleaned data to a new CSV file
    df_cleaned.to_csv('bbc_data_cleaned.csv', index=False)
    print("Cleaned data saved to bbc_data_cleaned.csv")

    # Verify the file was created
    if os.path.exists('bbc_data_cleaned.csv'):
        print("File bbc_data_cleaned.csv verified to exist.")
    else:
        print("Error: File bbc_data_cleaned.csv was not created.")
