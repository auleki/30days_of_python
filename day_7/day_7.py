it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1
# print(len(it_companies))

# 2
data = "Twitter"
it_companies.add(data)
# print(it_companies)

# 3
new_companies = {"Uber", "Hangout", "HP", "Dell"}
it_companies.update(new_companies)
# print(it_companies)

# 4 
it_companies.discard("Facebook")
# print(it_companies)

# 5
ans = """They are both methods that remove a value from the set, 
but the remove method throws an error if the value does not exist while the 
discard method throws no errors """
# print(ans)

# 6 
print(A.union(B))

# 7
print(A.intersection(B))

# 8
print(A.issubset(B))

# 9
print(A.isdisjoint(B))

# 10

# 11
print(A.symmetric_difference(B))

# 12 
del A, it_companies
# print(A, it_companies)

# 13
age_set = set(age)
print(age_set)

# 14 - 15 
# I will be back 



