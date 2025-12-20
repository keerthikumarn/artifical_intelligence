'''
File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.
'''
import os
import json

file = open('file_handling.py')
print(file)

txt = file.read()
print(type(txt))
print(txt)
#file.close()

# readlines(): read all the text line by line and returns a list of lines
lines = file.readlines()
print(type(lines))
print(lines)
file.close()


with open('sample.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
    
# using splitlines
file = open("sample.txt");
lines = file.read().splitlines()
print(type(lines))
print(lines)
file.close()

# Opening Files for Writing and Updating
with open("sample.txt", 'a') as new_file:
     new_file.write('Appending this new text..')
     
# The method below creates a new file, if the file does not exist:

with open('writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
    
# Deleting files
if os.path.exists('example1.txt'):
    os.remove('example1.txt')
else:
    print('The file does not exist')
    
if os.path.exists('writing_file_example.txt'):
    os.remove('writing_file_example.txt')
else:
    print('The file does not exist')
    
# File with JSON extension

person_dict= {
    "name":"Keerthi Kumar",
    "country":"India",
    "city":"Bangalore",
    "skills":["Java/J2EE", "System Design","Leadership"]
}

person_json = '''{
    "name": "Keerthi Kumar",
    "country": "India",
    "city": "Bangalore",
    "skills": ["Java/J2EE", "System Design","Leadership"]
}'''
# let's change JSON to dictionary
person_dictinoary = json.loads(person_json)
print(type(person_dictinoary))
print(person_dictinoary)
print(person_dictinoary['name'])
print(person_dictinoary['skills'])
print(person_json)

# Saving content as a JSON file
with open("person.json", "w", encoding='utf-8') as json_file:
    json.dump(person_dictinoary, json_file, ensure_ascii=False, indent=5)
