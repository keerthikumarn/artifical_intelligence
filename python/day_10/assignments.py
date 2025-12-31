# Iterate 0 to 10 using for loop, do the same using for loop.

for num in range(0, 11):
    print(num)
    
# Iterate 0 to 10 using for loop, do the same using while loop.
num = 0
while num <= 10:
    print(num)
    num+=1
    
for num in range(1, 8):
    print("#" * num)
    
for _ in range(8):
    print("# " * 8)
    
for num in range(0, 11):
    print(f"{num} x {num} = {num * num}")
    
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask', 'Java']

for language in languages:
    print(language)
    
# Use for loop to iterate from 0 to 100 and print only even numbers

for num in range(0, 101):
    if num % 2 == 0:
       print(num)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(0, 101):
    if num % 2 != 0:
       print(num)
       
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0

for num in range(0, 101):
    total += num

print(total)

'''
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
The sum of all evens is 2550. And the sum of all odds is 2500.
'''
sum_of_even_nums = 0
sum_of_odd_nums = 0

for num in range(0, 101):
    if num % 2 == 0:
        sum_of_even_nums += num
    else:
        sum_of_odd_nums += num

print("The sum of all evens is", sum_of_even_nums)
print("The sum of all odds is", sum_of_odd_nums)
