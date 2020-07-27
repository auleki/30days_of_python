# 1

dog = {}

# 3
student = {
    "first_name": "Eric",
    "last_name": "Carmen",
    "gender": "M",
    "marital_status": "Single",
    "skills": ["Basketball", "Movies", "Cooking", "Making music"],
    "country": "Nigeria",
    "city": "Lagos",
    "address": "White House"
}

# 4
# print(len(student))

# 5
skills_val = student.get("skills")
# print(type(skills_val))

# 6

skills_val.append("Hacking")
# print(student)

# 7 - 8
stu_keys = student.keys()

stu_values = student.values()

# 9
new_list = student.items()
# print(new_list)

# 10
print(student.popitem())

# 11
del student
# print(student)

