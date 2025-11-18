# Filtering only negative and zero numbers

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [number for number in numbers if number <= 0]
print(filtered_numbers)

# Flattening the list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist_1 in list_of_lists for sublist_2 in sublist_1 for number in sublist_2]
print(flattened_list)
