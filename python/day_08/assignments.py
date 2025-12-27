'''
Create an empty dictionary called dog Add name, color, breed, legs, age to the dog dictionary
'''
dog = {}

dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

print(dog)

'''
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
'''
student = {
    "first_name": "Keerthi",
    "last_name": "Kumar",
    "gender": "Male",
    "age": 40,
    "marital_status": "Married",
    "skills": ["Python", "Java"],
    "country": "India",
    "city": "Bengaluru",
    "address": "Uttarahalli"
}

print("Length of student dictionary:", len(student))
skills = student["skills"]
print("Skills:", skills)
print("Type of skills:", type(skills))

skills.append("Spring Boot")
skills.append("AWS")

print("\nUpdated student dictionary:")
print(student)
