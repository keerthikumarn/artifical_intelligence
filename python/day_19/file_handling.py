'''
File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.
'''

file = open('file_handling.py')
print(file)

txt = file.read()
print(type(txt))
print(txt)
file.close()

