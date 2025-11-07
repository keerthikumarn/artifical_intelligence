#Create an empty dictionary
empty_dict = {}

keerthi_dict = {'first_name':'Keerthi', 'last_name':'Kumar', 'designation':'Technical Architect', 'language':'Java'}
print(len(keerthi_dict))
print(keerthi_dict)

#Accessing the specific elements from dictionary
print(keerthi_dict['first_name'])
print(keerthi_dict['last_name'])
print(keerthi_dict['designation'])

keerthi_dict['company']='testing'

print(keerthi_dict)

keerthi_dict['company']='testing123'
print(keerthi_dict)

print('first_name' in keerthi_dict)

print('middle_name' in keerthi_dict)

#Changing Dictionary to a List of Items
print(keerthi_dict.items())

#to print only values from the dictionary
print(keerthi_dict.values())

# clear the dictionary

keerthi_dict.clear()
print(keerthi_dict)

