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

'''
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
'''
A_union_B = A.union(B)
print("A ∪ B:", A_union_B)

# 2. Find A intersection B
A_intersection_B = A.intersection(B)
print("A ∩ B:", A_intersection_B)

# 3. Check if A is a subset of B
print("Is A subset of B?:", A.issubset(B))

# 4. Check if A and B are disjoint sets
print("Are A and B disjoint?:", A.isdisjoint(B))

# 5. Join A with B and B with A (both give same result)
print("A joined with B:", A | B)
print("B joined with A:", B | A)

# 6. Symmetric difference between A and B
print("Symmetric Difference:", A.symmetric_difference(B))
