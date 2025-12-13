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
