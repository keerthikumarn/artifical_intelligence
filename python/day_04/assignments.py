# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ["Thirty", "Days", "Of", "Python"]
result = " ".join(words)
print(result)

company="test_company"
print("Company name: ", company)
print("Length of the String: ", company, "is: ", len(company))

print(company.upper())

words1 = ["Coding", "for", "All"]

coding = " ".join(words1)
print(coding)

index_of_C = coding.index('C')
index_of_f = coding.index('f')
print(index_of_C)
print(index_of_f)

'''
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
'''
sentence = 'You cannot end a sentence with because because because is a conjunction'
index_of_because = sentence.find('because')
print("First index of because: ",index_of_because)
index_of_last_because = sentence.rindex('because')
print("Last index of because: ", index_of_last_because)







