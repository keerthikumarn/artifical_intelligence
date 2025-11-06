first_name = 'Keerthi'
last_name = 'Kumar'
country = 'India'
city = 'Bangalore'
age = 40
is_married = True
skills = ['Java/J2EE', 'System Design', 'HLD and LLD', 'Springboot', 'Python']
person_info = {
    'firstname':'Keerthi', 
    'lastname':'Kumar', 
    'country':'India',
    'city':'Bangalore'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Keerthi', 'Kumar', 'Bangalore', 40, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
