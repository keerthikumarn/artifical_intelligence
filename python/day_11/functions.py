def generate_full_name():
   first_name = "Keerthi"
   last_name = "Kumar"
   space = " "
   full_name = first_name + space + last_name
   return full_name
   #print(full_name)
   
def add_two_numbers ():
    num_one = 21
    num_two = 76
    total = num_one + num_two
    #print(total)
    return total
    

print(add_two_numbers())
   
print(generate_full_name())


# function with parameters

def greet(name):
   message = name + ', welcome to Python for Everyone!'
   return message
   
print(greet("Keerthi Kumar"))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

# Passing Arguments with Key and Value

def display_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(display_fullname(firstname = 'Keerthi', lastname = 'Kumar'))


# Returning boolean value
def is_even_number(number):
    if number % 2 == 0:
       print("Even")
       return True
    return False

print(is_even_number(31))
print(is_even_number(36))

def are_unique_numbers(numbers):
    return len(numbers) == len(set(numbers))
    
print(are_unique_numbers([1, 2, 3, 4])) 	
print(are_unique_numbers([1, 2, 1, 4])) 
