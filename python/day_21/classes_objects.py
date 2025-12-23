'''
Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.
'''
class Person:
    pass
print(Person)

# creating an object
p = Person()
print(p)

class Student:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

stu = Student('Keerthi Kumar')
print(stu.name)
print(stu)
