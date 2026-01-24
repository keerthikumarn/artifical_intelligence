'''
Read the hacker_news.csv file from data directory
Get the first five rows
Get the last five rows
Get the title column as pandas series
Count the number of rows and columns
Filter the titles which contain python
Filter the titles which contain JavaScript
Explore the data and make sense of it
'''
import pandas as pd
import numpy as np
from collections import Counter
import re

# Reading CSV File Using Pandas
df = pd.read_csv('hacker_news.csv')
print(df)

# 1. First five rows
print("First 5 rows:")
print(df.head())

# 2. Last five rows
print("\nLast 5 rows:")
print(df.tail())

# 3. Title column as pandas Series
print("\nTitle column (Series):")
titles = df["title"]
print(titles)

# 4. Count rows and columns
rows, cols = df.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {cols}")

# 5. Filter titles containing 'python' (case-insensitive)
python_titles = df[df['title'].str.contains("python", case=False, na=False)]
print("\nTitles containing 'Python':")
print(python_titles["title"])

# 5. Filter titles containing 'javascript' (case-insensitive)
js_titles = df[df['title'].str.contains("javascript", case=False, na=False)]
print("\nTitles containing 'javascript':")
print(js_titles["title"])

# Exploring the data
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include="all"))

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTop 10 most common words in titles:")

all_words = " ".join(df["title"].dropna()).lower()
words = re.findall(r"\b\w+\b", all_words)
common_words = Counter(words).most_common(10)
print(common_words)
