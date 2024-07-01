import pandas as pd
import bar_chart_race as bcr

# Check if the cleaned data file exists
try:
    df = pd.read_csv('bbc_data_cleaned.csv')
    print("Cleaned data loaded successfully from bbc_data_cleaned.csv")
except FileNotFoundError:
    print("Error: bbc_data_cleaned.csv file not found.")
    exit()

# Ensure 'Date' column is the index and sorted
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# Print the first few rows to verify data
print("First few rows of the cleaned data:")
print(df.head())

# Generate the bar chart race
bcr.bar_chart_race(df, filename='bbc_data_race.mp4', n_bars=10, period_length=500)
print("Bar chart race saved to bbc_data_race.mp4")
