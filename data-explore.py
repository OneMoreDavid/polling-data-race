import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='data_examination.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting data examination process")

# Load the CSV file
try:
    df = pd.read_csv('bbc_data.csv')
    logging.info("Data loaded successfully from bbc_data.csv")
except FileNotFoundError:
    logging.error("Error: bbc_data.csv file not found.")
    exit()

# Print the first few rows of the DataFrame
logging.debug("First few rows of the data:\n%s", df.head())

# Print summary statistics
logging.debug("Summary statistics:\n%s", df.describe(include='all'))

# Identify missing values
logging.debug("Missing values:\n%s", df.isnull().sum())

# Print data types
logging.debug("Data types:\n%s", df.dtypes)
