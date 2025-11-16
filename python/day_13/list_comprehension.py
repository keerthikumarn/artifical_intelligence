#basic way
language='Java'
my_list=list(language)
print(type(my_list))
print(my_list)

#list comprehension way
new_list = [lang for lang in language]
print(type(new_list))
print(new_list)

# Generating numbers
numbers = [number for number in range(15)]
print(type(numbers))
print(numbers)

# printing square of numbers
squares = [number * number for number in range(10)]
print(squares)

# List of tuples
tuples = [(number, number * number) for number in range (11)]
print(tuples)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

# Lambda functions
add_numbers=lambda num1, num2: num1 + num2
print(add_numbers(45,22))
