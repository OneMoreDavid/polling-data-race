import requests
from bs4 import BeautifulSoup
import pandas as pd
import bar_chart_race as bcr

# Step 1: Scrape the data
url = 'https://www.bbc.co.uk/news/articles/cyxx9vxwjk9o'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')  # Adjust this to the correct table if there are multiple

# Extract the table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the table rows
rows = table.find_all('tr')[1:]  # Skip the header row

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == len(headers):
        data.append([cell.text.strip() for cell in cells])
    else:
        print(f"Row skipped due to mismatch in columns: {row}")

# Step 2: Parse the data into a DataFrame
df = pd.DataFrame(data, columns=headers)

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Handle missing or invalid dates
df.dropna(subset=['Date'], inplace=True)

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Check the DataFrame structure
print(df.head())

# Step 3: Create the bar-chart race
bcr.bar_chart_race(df, filename='bbc_data_race.mp4', n_bars=10, period_length=500)
