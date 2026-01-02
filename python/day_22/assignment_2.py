'''
Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
'''
import requests
from bs4 import BeautifulSoup
import json

url = "https://archive.ics.uci.edu/datasets"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

datasets = []

cards = soup.find_all("div", class_="rounded-box", attrs={"role": "row"})
print("Dataset cards found:", len(cards))

for card in cards:
    try:
        name_tag = card.find("h2").find("a")
        name = name_tag.get_text(strip=True)
        link = "https://archive.ics.uci.edu" + name_tag["href"]

        description = card.find("p").get_text(strip=True)

        meta = card.find_all("span", class_="truncate")

        dataset = {
            "name": name,
            "url": link,
            "description": description,
            "task": meta[0].get_text(strip=True) if len(meta) > 0 else None,
            "data_type": meta[1].get_text(strip=True) if len(meta) > 1 else None,
            "instances": meta[2].get_text(strip=True) if len(meta) > 2 else None,
            "features": meta[3].get_text(strip=True) if len(meta) > 3 else None,
        }

        datasets.append(dataset)

    except Exception:
        continue

with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(datasets, f, indent=4, ensure_ascii=False)

print(f"Extracted {len(datasets)} datasets")
print("Done! Data written to uci_datasets.json")

