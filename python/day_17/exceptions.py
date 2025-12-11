try:
    print(10 + '5')
except:
    print('Something went wrong')
    
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
    
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
    
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
    
    
# Packing and Unpacking Arguments in Python
def sum_of_five_numbers(num1, num2, num3, num4, num5):
   return num1 + num2 + num3 + num4 + num5
   
num_list = [1 ,3, 5, 7, 9]
# print(sum_of_five_numbers(num_list))
print(sum_of_five_numbers(*num_list)) 

countries = ['India', 'Australia', 'France', 'England', 'NewZealand']
ind, aus, fra, *rest = countries
print(ind, aus, fra, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)   
