empty_tuple = ()

#tuple with initial values

fruits = ('Mango', 'Banana', 'Avocado', 'Water melon')
print("Total fruits available in the tuple", len(fruits))

all_fruits = fruits[0:4]
print(all_fruits)

all_fruits = fruits[0:]
print(all_fruits)

middle_two_fruits = fruits[1:3]
print(middle_two_fruits)

# check if an element/item exists
print('Mango' in fruits)
print('Orange' in fruits)

vegetables = ('Tomato', 'Brinjal', 'Carrot');

mixed = vegetables + fruits

print(mixed)
