import re
from collections import Counter


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

