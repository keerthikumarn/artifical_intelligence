# Filtering only negative and zero numbers

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [number for number in numbers if number <= 0]
print(filtered_numbers)
