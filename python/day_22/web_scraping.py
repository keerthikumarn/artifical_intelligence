'''
What is Web Scrapping
The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.
Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
'''

import requests
from bs4 import BeautifulSoup

#url = 'https://archive.ics.uci.edu/ml/datasets.php'
#url = 'https://example.com'
url = 'https://quotes.toscrape.com'
#url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
status = response.status_code
print(status)
content = response.content
#print(content)
soup = BeautifulSoup(content, 'html.parser')
#print(soup)

print(soup.title)
print(soup.title.get_text())
print(soup.body)
