'''
Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.
'''
class Person:
    pass
print(Person)

# creating an object
p = Person()
print(p)

# Object Methods
class Student:
      def __init__ (self, name, age, email):
        # self allows to attach parameter to the class
          self.name =name
          self.age = age
          self.email = email
          
      def student_info(self):
        return f'{self.name} is {self.age} years old. His email id is: {self.email}'

stu = Student('Keerthi Kumar', 40, 'keerthi@no-reply.com')
print(stu.name)
print(stu.age)
print(stu.email)
print(stu.student_info())
print(stu)
