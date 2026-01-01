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
