import requests
from bs4 import BeautifulSoup
import pandas as pd
import bar_chart_race as bcr

# Step 1: Scrape the data
url = 'https://www.bbc.co.uk/news/articles/cyxx9vxwjk9o'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')  # Modify this line according to the specific HTML structure

# Extract the table data
data = []
headers = [header.text for header in table.find_all('th')]
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    data.append([cell.text for cell in cells])

# Step 2: Parse the data into a DataFrame
df = pd.DataFrame(data, columns=headers)
df['Date'] = pd.to_datetime(df['Date'])  # Adjust column names as necessary
df.set_index('Date', inplace=True)

# Step 3: Create the bar-chart race
bcr.bar_chart_race(df, filename='bbc_data_race.mp4', n_bars=10, period_length=500)
