#while loop
print("starting with the basic while loop")
count = 0
while count < 5:
   print(count)
   count = count + 1
else:
    print(count)
    
    
# break statement
print("starting with break in while loop")
counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1
    if counter == 2:
        print("break loop encountered")
        break
        
# continue statement
print("starting with continue in while loop")
counter1 = 0
while counter1 < 5:
    if counter1 == 3:
        counter1 = counter1 + 1
        continue
    print(counter1)
    counter1 = counter1 + 1
    
    
# For loop
numbers = [0, 1, 2, 3, 4, 5]
print("Starting with the basic for loop")
for number in numbers:
    print(number)
    

language="Springboot"
for letter in language:
   print(letter)
   
person = {
    'first_name':'Keerthi',
    'last_name':'Kumar',
    'age':40,
    'country':'India',
    'is_marred':True,
    'skills':['Java', 'Springboot', 'Postgres', 'System Design', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'560061'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
    
    
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    
    
num = (0,1,2,3,4,5)
for number in num:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')    

