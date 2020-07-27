# 1

# age = int(input("> Enter your age: "))
# legal_age = 18
# years_left = legal_age - age
#
# if age > 18:
#     print("You are old enough to drive")
# else:
#     print(f"You need {years_left} more years to learn to drive")
#


# 2

# my_age = int(input("> My Age: "))
# your_age = int(input("> Your Age: "))
# difference = abs(my_age - your_age)
#
# if difference == 1:
#     if my_age > your_age:
#         print(f"I am {difference} year older")
#     else:
#         print(f"You are {difference} year older")
# elif my_age > your_age:
#     print(f"I am {difference} years older than you")
# elif my_age == your_age:
#     print(f"We are both {my_age} years old")
# else:
#     print(f"You are {difference} years older than me")

# 3
#
# a = int(input("> Pick A number: "))
# b = int(input("> Pick B number "))
#
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a == b:
#     print(f"{a} is equal to {b}")
# else:
#     print(f"{a} is smaller than {b}")


# 4

# name = input("> Your name please... ")
# grading = int(input(f"> {name} what is your score? : "))
#
# if grading > 100:
#     print(f"Wawu {name} 😂 you can't score above 100")
# elif grading >= 80:
#     print(f"Congratulations, {name} you got an A 🎉")
# elif 80 > grading >= 70:
#     print(f"{name} you got a B")
# elif 70 > grading >= 60:
#     print(f"{name} you got a C")
# elif 50 <= grading < 60:
#     print(f"{name} you got a D")
# else:
#     print(f"{name} you got a F, you mom won't like that")

# 5

# autumn = ["september", "october", "november"]
# winter = ["december", "january", "february"]
# spring = ["march", "april", "may"]
# summer = ["june", "july", "august"]
#
# season = input("> What month is it?: ").lower()
# if season in autumn:
#     print("The season is Autumn")
# elif season in winter:
#     print("The season is Winter")
# elif season in spring:
#     print("The season is Spring")
# elif season in summer:
#     print("The season is Summer")
# else:
#     print("Your input is part of our 12 month calendar")

# 6
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
#
# new_fruit = input("> Give us a fruit: ").lower()
#
# if new_fruit not in fruits:
#     fruits.append(new_fruit)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')

# 7

person = {
    "first_name": "Wahab",
    "last_name": "Giwa",
    "age": 35,
    "country": "Nigeria",
    "is_married": False,
    "skills": ["Javascript", "React", "NodeJs", "MongoDB", "SQL", "GraphQL", "Python"],
    "address": {
        "street": "24 Look well street",
        "zipcode": "02210"
    }

}

# i
#
# skills = person.get("skills")
# search = "skills"
# print(skills[-3:-1]) if search in person.keys() else print("No such key")


# ii

requirements = "Python"
search = "skills"

if search in person.keys() and requirements in person.get("skills"):
    print(person.get("skills"))
else:
    print("Python language is a requirement for this role")

 # iii
# Returning back here




