from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
print(np_normal_dis)

print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

# plot the graph
plt.hist(np_normal_dis, color="green", bins=21)
plt.show()
