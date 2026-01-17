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

even_numbers = np.arange(2, 20, 2)
print(even_numbers)

# Creating sequence of numbers using linspace
np.linspace(1.0, 5.0, num=10)
# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)

# NumPy Statistical Functions with Example
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))
print('sd: ', two_dimension_array.std())

# repeating sequences
arr =[1 ,2, 5]
print('Tile:   ', np.tile(arr, 3))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(arr, 3))

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)


# Generating random numbers
normal_arr = np.random.normal(79, 15, 80)
print(normal_arr)

sns.set()
plt.hist(normal_array, color="grey", bins=50)

np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
