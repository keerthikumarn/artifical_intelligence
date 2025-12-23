import requests
import statistics
from collections import defaultdict

'''Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats'''

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api)
cats = response.json()

print(cats)

def get_midpoint(range_str):
    try:
    	low, high = map(float, range_str.split("-"))
    	return (low + high) / 2
    except:
        return None
        
weights = []
lifespans = []

country_breed_freq = defaultdict(lambda: defaultdict(int))

for cat in cats:
    # Weight (metric)
    weight = get_midpoint(cat.get("weight", {}).get("metric", ""))
    if weight is not None:
        weights.append(weight)

    # Life span
    lifespan = get_midpoint(cat.get("life_span", ""))
    if lifespan is not None:
        lifespans.append(lifespan)

    # Country vs Breed frequency
    country = cat.get("origin", "Unknown")
    breed = cat.get("name", "Unknown")
    country_breed_freq[country][breed] += 1

# -----------------------------
# Statistical calculations
# -----------------------------
def stats(values):
    return {
        "min": min(values),
        "max": max(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "std_dev": statistics.stdev(values)
    }

weight_stats = stats(weights)
lifespan_stats = stats(lifespans)


print(" Cat Weight Statistics (kg)")
for k, v in weight_stats.items():
    print(f"{k}: {round(v, 2)}")

print("\n Cat Lifespan Statistics (years)")
for k, v in lifespan_stats.items():
    print(f"{k}: {round(v, 2)}")

print("\n Country vs Breed Frequency Table")
for country, breeds in country_breed_freq.items():
    print(f"\n{country}")
    for breed, count in breeds.items():
        print(f"  {breed}: {count}")

