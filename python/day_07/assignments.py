it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
'''
print("Length of it_companies:", len(it_companies))
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)
it_companies.update({'Netflix', 'Intel', 'Adobe'})
print("After adding multiple companies:", it_companies)
it_companies.remove('IBM') 
print("After removing one company:", it_companies)
