'''
Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
'''
import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find the first table on the page (the presidents table)
table = soup.find("table", {"class": "wikitable"})

presidents = []

if not table:
    print("No table found!")
else:
    rows = table.find_all("tr")

    for row in rows[1:]:  # skip header
        cells = row.find_all(["th","td"])
        if len(cells) < 6:
            continue

        # Extract basic fields
        order = cells[0].get_text(strip=True)
        name = cells[1].get_text(strip=True)
        life = cells[2].get_text(strip=True)
        term = cells[3].get_text(strip=True)
        party = cells[4].get_text(strip=True)
        vp = cells[5].get_text(strip=True)

        presidents.append({
            "order": order,
            "name": name,
            "lifespan": life,
            "term": term,
            "party": party,
            "vice_president": vp
        })

# Write JSON
with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4, ensure_ascii=False)

print(f"Extracted {len(presidents)} presidents")
print("Saved to us_presidents.json")
