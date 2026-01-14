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
