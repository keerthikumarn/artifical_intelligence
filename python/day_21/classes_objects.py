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
          self.skills = []
          
      def student_info(self):
        return f'{self.name} is {self.age} years old. His email id is: {self.email}'
        
      def add_skill(self, skill):
          self.skills.append(skill)

stu = Student('Keerthi Kumar', 40, 'keerthi@no-reply.com')
print(stu.name)
print(stu.age)
print(stu.email)
print(stu.student_info())
print(stu)

s1 = Student('Keerthi Kumar', 40, 'keerthi@no-reply.com')
s2 = Student('Rohith', 45, 'rohith@no-reply.com')
print(s1.student_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.student_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
