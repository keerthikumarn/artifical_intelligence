import re
from collections import Counter
import keyword


'''
What is the most frequent word in the following paragraph? paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do 
not love something which can give you all the capabilities to develop an application what else can you love.
'''
paragraph = (
    "I love teaching. If you do not love teaching what else can you love. "
    "I love Python if you do not love something which can give you all the "
    "capabilities to develop an application what else can you love."
)


words = re.findall(r'\b\w+\b', paragraph)
word_counter = Counter(words);

print(words)
print(word_counter)

result = sorted(
    [(count, word) for word, count in word_counter.items()],
    key=lambda x: (-x[0], x[1])
)

print(result)

'''
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
'''

def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name)) and not keyword.iskeyword(name)
    
# Test cases
print(is_valid_variable('first_name'))      # True
print(is_valid_variable('first-name'))      # False (contains hyphen)
print(is_valid_variable('1first_name'))     # False (starts with digit)
print(is_valid_variable('firstname'))       # True
print(is_valid_variable('_private'))        # True (underscore is valid)
print(is_valid_variable('class'))           # False (Python keyword)
print(is_valid_variable('my_var_123'))      # True
print(is_valid_variable(''))                # False (empty string)
