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
