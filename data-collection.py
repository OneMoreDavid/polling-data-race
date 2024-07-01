import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the BBC article
url = 'https://www.bbc.co.uk/news/articles/cyxx9vxwjk9o'

# Request the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')  # Adjust this to the correct table if there are multiple

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]
print("Headers:", headers)  # Debug print

# Extract rows
rows = table.find_all('tr')[1:]  # Skip the header row

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == len(headers):
        data.append([cell.text.strip() for cell in cells])
    else:
        print(f"Row skipped due to mismatch in columns: {row}")

# Create a DataFrame and save to CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv('bbc_data.csv', index=False)
print("Data saved to bbc_data.csv")

# Print the first few rows of the DataFrame to verify data
print("First few rows of the collected data:")
print(df.head())
