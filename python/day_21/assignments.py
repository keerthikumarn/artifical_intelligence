'''
Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
'''
class Statistics:
     def __init__(self, data):
         self.data = sorted(data)
       
     def count(self):
         return len(self.data)
         
     def sum(self):
        return sum(self.data)

     def min(self):
        return self.data[0]

     def max(self):
        return self.data[-1]

     def range(self):
        return self.max() - self.min()
        
     def mean(self):
        return round(self.sum() / self.count())
        
     
     def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

     def mode(self):
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1
        max_count = max(freq.values())
        mode_value = min(k for k, v in freq.items() if v == max_count)
        return {"mode": mode_value, "count": max_count}
        
     def std(self):
        return round(self.var() ** 0.5, 1)
        
     def percentile(self, p):
        k = (self.count() - 1) * (p / 100)
        f = int(k)
        c = min(f + 1, self.count() - 1)
        return self.data[f] + (self.data[c] - self.data[f]) * (k - f)
        
     def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return round(variance, 1)
        
     def freq_dist(self):
        freq = {}
        for value in self.data:
            freq[value] = freq.get(value, 0) + 1

        result = []
        for k, v in freq.items():
            percent = round((v / self.count()) * 100, 1)
            result.append((percent, k))
        return sorted(result, reverse=True)
         
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count())                       # 25
print('Sum:', data.sum())                           # 744
print('Min:', data.min())                           # 24
print('Max:', data.max())                           # 38
print('Range:', data.range())                       # 14
print('Mean:', data.mean())                         # 30
print('Median:', data.median())                     # 29
print('Mode:', data.mode())                         # {'mode': 26, 'count': 5}
print('Standard Deviation:', data.std())            # 4.2
print('Variance:', data.var())                      # 17.5
print('Frequency Distribution:', data.freq_dist())
