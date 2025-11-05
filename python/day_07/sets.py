fruits = {'banana', 'orange', 'mango', 'lemon'}

print(fruits)

print(len(fruits))

print("Does set fruits contain Dragon Fruit? ", 'Dragon Fruit' in fruits)

print("Does set fruits contain Mango? ", 'mango' in fruits)

fruits.add('papaya')

print(fruits)

fruits.update(['gauva','apple'])

print(fruits)

print(fruits.pop()) #removes a random element from the set
print(fruits)

#empty the set
fruits.clear()
print(fruits)
