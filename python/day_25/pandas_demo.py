'''
Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:

reshaping, merging, sorting, slicing, aggregation
'''
import pandas as pd
import numpy as np

# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# Creating Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ["Banana", "Butterfruit", "Mango"]
fruits = pd.Series(fruits, index = [1,2,3])
print(fruits)

# Creating Pandas Series from a Dictionary
keerthi_dict = {'first_name':'Keerthi', 'last_name':'Kumar', 'country':'India','city':'Bengaluru'}
s = pd.Series(keerthi_dict)
print(s)

# Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# Creating DataFrames from List of Lists
data = [
    ['Keerthi Kumar', 'India', 'Bangalore'],
    ['Pradeep', 'India', 'Shivmogga'],
    ['Gautam', 'India', 'Mangalore']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
dataset = {'Name': ['Keerthi Kumar', 'Gautam', 'Raghav'], 'Country':[
    'India', 'UK', 'France'], 'City': ['Bangalore', 'Stockholm', 'Antibes']}
df = pd.DataFrame(dataset)
print(df)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Keerthi Kumar', 'Country': 'India', 'City': 'Bangalore'},
    {'Name': 'Raghav Nayak', 'Country': 'UK', 'City': 'London'},
    {'Name': 'Vineeth', 'Country': 'France', 'City': 'Antibes'}]
df = pd.DataFrame(data)
print(df)

# Reading CSV File Using Pandas
data_frame = pd.read_csv('weight-height.csv')
print(data_frame)
print(data_frame.head()) #prints first 5 rows from the dataset
print(data_frame.tail()) #prints last 5 rows from the dataset
print(data_frame.shape)
print(data_frame.columns)
heights = data_frame['Height'] # new series
print(heights)
weights = data_frame['Weight'] # new series
print(weights)
print(len(heights) == len(weights))
print(heights.describe()) # give statistical information about height data 
print(weights.describe()) # give statistical information about weight data
print(data_frame.describe())  # describe can also give statistical information from a dataFrame

# Creating a DataFrame
data = [
    {"Name": "Keerthi Kumar", "Country":"India","City":"Bangalore"},
    {"Name": "Chenna Reddy", "Country":"UK","City":"London"},
    {"Name": "Raghav Nayak", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
