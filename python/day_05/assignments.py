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

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print("Sorted Ages:", ages)

# Find min and max age
min_age = min(ages)
max_age = max(ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

# Add min and max again to the list
ages.append(min_age)
ages.append(max_age)
print("List after adding min and max again:", ages)

# Find the median age
ages.sort()
n = len(ages)
if n % 2 == 1:  # odd number of items
    median_age = ages[n // 2]
else:  # even number of items
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
print("Median Age:", median_age)

# Find the average age
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

# Find the range of ages
age_range = max_age - min_age
print("Age Range:", age_range)

# Compare (min - average) and (max - average)
comparison_min = abs(min_age - average_age)
comparison_max = abs(max_age - average_age)
print("abs(min - average):", comparison_min)
print("abs(max - average):", comparison_max)
