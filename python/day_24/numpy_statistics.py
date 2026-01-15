import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

normal_array = np.random.normal(
    loc=0,      # mean
    scale=1,    # standard deviation
    size=10000  # number of samples
)

sns.set()
plt.hist(normal_array, color="grey", bins=50)

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# Numpy numpy.arange()
'''
Sometimes, you want to create values that are evenly spaced within a defined interval. For instance, you want to create values from 1 to 10; you can use numpy.arange() function
'''

# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
for l in lst:
    print(l)
    
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)
