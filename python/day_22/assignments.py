'''
Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
'''

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bu.edu/president/boston-university-facts-stats/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = {}

# BU facts are stored in definition lists
dl_tags = soup.find_all("dl")

print("DL tags found:", len(dl_tags))

for dl in dl_tags:
    terms = dl.find_all("dt")
    values = dl.find_all("dd")

    for term, value in zip(terms, values):
        key = term.get_text(strip=True)
        val = value.get_text(strip=True)
        data[key] = val

print("Extracted records:", len(data))

with open("bu_facts_stats.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Done! Data written to bu_facts_stats.json")

