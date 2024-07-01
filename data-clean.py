import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(filename='data_cleaning.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting data cleaning process")

# Load the CSV file
try:
    df = pd.read_csv('bbc_data.csv')
    logging.info("Data loaded successfully from bbc_data.csv")
except FileNotFoundError:
    logging.error("Error: bbc_data.csv file not found.")
    exit()

# Print the first few rows of the DataFrame to verify data
logging.debug("First few rows of the collected data:\n%s", df.head())

# Check if 'Date' column exists
if 'Date' not in df.columns:
    logging.error("Error: 'Date' column not found in the data. Available columns: %s", df.columns)
else:
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    logging.info("Converted 'Date' column to datetime format")

    # Drop rows with missing or invalid dates
    df_cleaned = df.dropna(subset=['Date'])
    logging.info("Dropped rows with missing or invalid dates")

    # Additional cleaning steps can be added here

    # Save the cleaned data to a new CSV file
    df_cleaned.to_csv('bbc_data_cleaned.csv', index=False)
    logging.info("Cleaned data saved to bbc_data_cleaned.csv")

    # Verify the file was created
    if os.path.exists('bbc_data_cleaned.csv'):
        logging.info("File bbc_data_cleaned.csv verified to exist.")
    else:
        logging.error("Error: File bbc_data_cleaned.csv was not created.")
