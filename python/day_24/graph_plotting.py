from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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


temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
