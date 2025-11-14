import modules
from statistics import *
import math

print(modules.generate_full_name('Keerthi', 'Kumar')) 

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print("Mean value of ages :", mean(ages))
print("Median value of ages :", median(ages))
print("stdev value of ages :", stdev(ages))
print("Mode value of ages :", mode(ages))

print("PI value: ", math.pi)
print("Power of: ", math.pow(2, 3))
print("Floor value: ", math.floor(9.81)) 
print("Rounding of the value: ", math.ceil(9.81))
print("Logarithm value: ", math.log10(100))
