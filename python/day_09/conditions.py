num = 0
if num > 0:
    print('num is a positive number')
elif num < 0:
    print('num is a negative number')
else:
    print('num is zero')
    
    
a = 17
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
    
    
user = 'Keerthi'
access_level = 2
if user == 'Keerthi' or access_level >= 2:
        print('Access granted!')
else:
    print('Access denied!')
