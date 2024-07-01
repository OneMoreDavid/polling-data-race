import pandas as pd
import bar_chart_race as bcr

# Load the cleaned CSV file
df = pd.read_csv('bbc_data_cleaned.csv')

# Ensure 'Date' column is the index and sorted
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

# Generate the bar chart race
bcr.bar_chart_race(df, filename='bbc_data_race.mp4', n_bars=10, period_length=500)
print("Bar chart race saved to bbc_data_race.mp4")
