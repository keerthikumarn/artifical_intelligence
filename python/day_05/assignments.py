'''
Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
'''
mixed_data_types = ["Keerthi Kumar N", 40, 5.4, "Married", "Bangalore, KA, INDIA"]
print(mixed_data_types)


first_item = mixed_data_types[0]
middle_item = mixed_data_types[len(mixed_data_types) // 2]
last_item = mixed_data_types[-1]

print("First Element:", first_item)
print("Middle Element:", middle_item)
print("Last Element:", last_item)

'''
Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
'''
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("List of IT companies: ", it_companies)
print("No. of companies in the list: ",len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company= it_companies[-1]

print("First Company:", first_company)
print("Middle Company:", middle_company)
print("Last Company:", last_company)

it_companies.append("Amadeus")
print("No. of companies in the list: ",len(it_companies))

# change one of the it_company to upper case
it_companies[2] = it_companies[2].upper()
print(it_companies)

# Check if a certain company exists in the it_companies list.
company_to_check = "Google"

if company_to_check.upper() in [company.upper() for company in it_companies]:
    print(f"{company_to_check} exists in the list")
else:
    print(f"{company_to_check} does not exist in the list")
    

# sorting the companies
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)
