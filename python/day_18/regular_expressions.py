'''
A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. 
To use RegEx in python first we should import the RegEx module which is called re.
'''

import re
txt = 'I love to teach Java and Devops'
match = re.match('I love to teach', txt, re.I)
print(match)
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)

# Find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)

# not matching
not_match = re.match('I like to teach', txt, re.I)
print(not_match) 


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']


# without custom pattern
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']


matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

#  The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text.
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))
