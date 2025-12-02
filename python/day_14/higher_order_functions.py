def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(5))
result = higher_order_function('cube')
print(result(9))
result = higher_order_function('absolute')
print(result(-4))

# Python Closures
'''
Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. 
In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. 
'''

def add_ten():
    value = 10
    def add(num):
        return num + value
    return add

closure_result = add_ten()
print(closure_result(-17))
print(closure_result(-32))

# Python Decorators
'''
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate.
'''
def greet():
  return "Welcome to python programming"
  
def uppercase_decorator(function):
   def wrapper():
      func = function()
      make_uppercase = func.upper()
      return make_uppercase
   return wrapper
   
greeting_message = uppercase_decorator(greet)
print(greeting_message())

# Applying multiple decorators to a single function

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to the world of python programming!'
print(greeting())
