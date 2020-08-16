# 1
def add_two(num1, num2):
  return num1 + num2

# 2
def area_of_circle(r, pie=3.14):
  return pie * r * r
result = area_of_circle(22.6)


# 3
# 

# 4

def calc_to_farh(temp):
  toFah = temp * 9/5 + 32
  return f"Temperature is: {toFah}"

result = calc_to_farh(36)

# 5 

def check_season(season):
  if(season == 'Autumn'):
    print('It is Autumn')
  elif(season == 'Winter'):
    print('It is Winter')
  elif(season == 'Spring'):
    print('It is Spring')
  elif(season == 'Summer'):
    print('It is Summer')
  else:
    print("No such season")

# check_season("Spring")

# 6
#  def calculate_slope:
#    return 

# 7

# def solve_quadratic_eqn(a, b, c, x):
#   x_square = x * x
#   return (a * x_square) + (b * x) + c

# result = solve_quadratic_eqn(5, 3, 1, 4)
# print(result)

# 8

# digits = [9, 0, 23, 55, 98]

# def print_list(list):
#   for i in list:
#     print(i)

# print_list(digits)


# 9 - 10

# 11
genres = ['Action', 'Horror', 'Drama']

def add_item(genres, newGenre):
  genres.append(newGenre)
  print(genres)
# add_item(genres, 'Comedy')

# 12
# BRB



# 13
def sum_of_numbers(num):
  total = 0 
  for i in range(num):
    total += i 
    print(f"ref: {i}")
    print(total)

# sum_of_numbers(6)

# 14
def sum_of_odds(num):
  total = 0 
  for i in range(num):
    if(i % 2 != 0):
      total += i
      print(i)
    print(f"total: {total}")

# sum_of_odds(7)

# 15

def sum_of_evens(num):
  total = 0
  for i in range(num):
    if(i % 2 == 0):
      total += i
      print(i)
      print(f"total: {total}")

# sum_of_evens(6)

# 16
def even_and_odds(num):
  odds = []
  even = []
  for i in range(num):
    if (i % 2 == 0):
      even.append(i)
      # print(even)
    else:
      odds.append(i)
      # print(odds)
  print(f"Even: {even}")
  print(f"Odds: {odds}")

      
# even_and_odds(50)

# 17

def factorial(num):
  factorial = 1
  for i in range(1, num + 1):
    factorial *= i
    print(i)
  print(factorial)

# factorial(3)

# 18
def is_empty(data):
  if(len(data) < 0):
    print("You need to put in some data")
  else:
    print("Your info is being processed")

is_empty('lice')
# BRB NOT FINISHED

# 19





