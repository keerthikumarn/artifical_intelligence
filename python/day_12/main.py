import modules
from statistics import *

print(modules.generate_full_name('Keerthi', 'Kumar')) 

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print("Mean value of ages :", mean(ages))
print("Median value of ages :", median(ages))
print("stdev value of ages :", stdev(ages))
print("Mode value of ages :", mode(ages))
