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

