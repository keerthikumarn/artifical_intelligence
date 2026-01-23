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

