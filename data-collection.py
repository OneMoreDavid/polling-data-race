import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='data_collection.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# URL of the BBC article
url = 'https://www.bbc.co.uk/news/articles/cyxx9vxwjk9o'

logging.info("Starting data collection process")

# Request the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table in the HTML
table = soup.find('table')
if not table:
    logging.error("Error: No table found in the HTML content")
    exit()

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]
logging.debug("Headers: %s", headers)

# Extract rows
rows = table.find_all('tr')[1:]  # Skip the header row

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == len(headers):
        data.append([cell.text.strip() for cell in cells])
    else:
        logging.warning("Row skipped due to mismatch in columns: %s", row)

# Create a DataFrame and save to CSV
df = pd.DataFrame(data, columns=headers)
df.to_csv('bbc_data.csv', index=False)
logging.info("Data saved to bbc_data.csv")

# Print the first few rows of the DataFrame to verify data
logging.debug("First few rows of the collected data:\n%s", df.head())
