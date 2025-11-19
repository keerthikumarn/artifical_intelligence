# Filtering only negative and zero numbers

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [number for number in numbers if number <= 0]
print(filtered_numbers)

# Flattening the list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist_1 in list_of_lists for sublist_2 in sublist_1 for number in sublist_2]
print(flattened_list)

# Flattening the list - 1
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = []

for[(country, capital)] in countries:
   result.append([
   	country.upper(),
   	country[:3].upper(),
   	capital.upper()
   ])
   
print(result)
