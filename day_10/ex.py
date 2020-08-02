# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
#

cars = ["Benz", "Toyota", "Mazda", "Mistbuishi"]

# for car in cars:
#     print(f"{car} is King") if car == "Benz" else print(f"{car} is also a good choice")
#

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# print(person.items())

# for key, value in person.items():
#     print(f"key: {key}, value: {value}")



# for letter in "Python":
#     if letter == "h":
#         continue
#     print("Current letter:", letter)


# dig = 10
# while dig > 0:
#     dig = dig - 1
#     if dig == 7:
#         print(f"{dig} here, RUN!!")
#         continue
#     print("Current Variable Value:", dig)
# print("The end!")

# numbers = (0, 1, 2, 3, 4, 5)
# for num in numbers:
#     print(num)
#     if num == 3:
#         continue
#     print("Next number should be", num + 1) if num != 5 else print(f"{num + 1} is the end of loop")
# print("Out of loop")
#

# newList = list(range(21))
#
# print(newList)
# def timesX(digit):
#     for num in newList:
#         print(f"{num} * {digit} = {num * digit}")
#
# timesX(5)
#
#
#

# newList = list(range(1, 11, 2))
# print(newList)


for iterator in range(1, 10, 2):
    print(iterator)
else:
    print("Range is exhausted")




