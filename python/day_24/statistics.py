import numpy as np

print('numpy:', np.__version__)
#print(dir(np))

# Creating numpy arrays
python_list = [4,5,6,7,8,9]
print('Type:', type (python_list))
print(python_list)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list)) # <class 'numpy.ndarray'>
print(numpy_array_from_list)

# Creating float numpy arrays

python_list = [1,2,3,4,5]
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])


