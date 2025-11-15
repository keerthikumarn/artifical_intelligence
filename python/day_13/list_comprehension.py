#basic way
language='Java'
my_list=list(language)
print(type(my_list))
print(my_list)

#list comprehension way
new_list = [lang for lang in language]
print(type(new_list))
print(new_list)
