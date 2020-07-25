# 1 - 3
''' # COMING BACK '''

# 3 - 15
company = 'Coding For All'
change = "Python for Everyone"
text = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(company)
print(len(company))
lower_company = company.lower()
upper_company = company.upper()
capitalize = company.capitalize()
title = company.title()
swapcase = company.swapcase()
sliced = company[6:]
# print(sliced)
find_coding = company.find('Coding')
replace = company.replace('Coding', 'Python')
replace_2 = change.replace("Everyone", "All")
give_space = company.split(" ")
comma_split = text.split(",")
company_index = company[0]
company_last_index = company[-1]
find_with_index = company.index('C')
find_with_index = company.index('F')

# 22 Not completed
# what is rfind and rindex
# To find last occurence 
from_behind = company[:-3]
last_occurence = from_behind.find('l')
print(from_behind)

phrase = 'You cannot end a sentence with because because because is a conjuction'
find_first = phrase.find('because')


# 23 - 27

#28 - 30
company = '     Coding For All   '

starts_with = company.startswith('Coding')
ends_with = company.endswith('coding')
trim_company = company.strip()
print(trim_company)
print(company)

# 31
''' thirty_days_of_python '''

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

hashed = '# '.join(python_libraries)

print(hashed)

# 33 - 34
print("I am enjoying this challenge \nI just wonder what is next")

print("Name\t Age\t Country \nWahab\t 100\t Nigeria")

# 35
radius = 10
area = 3.14 * radius ** 2
result = 'The area of radius {} is {} meters square'.format(radius, area)
print(result)

# 36

