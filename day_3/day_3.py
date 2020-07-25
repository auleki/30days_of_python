# 1 - 3
age = int(26)
height = float(10)
complex_num = complex(2, -5)

#4

def calculate_circle_area(base, height):
    area = base * height * 0.5
    return area

base = int(input(">Base of the triangle? \n "))
height = int(input(">Height of the traingle  \n "))

area = calculate_circle_area(base, height)

# see result
print(f"Area of circle: {area}")


#5

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

side_a = int(input(">Enter side a: \n "))
side_b = int(input(">Enter side b: \n "))
side_c= int(input(">Enter side c: \n "))

perimeter = calculate_perimeter(side_a, side_b, side_c)
print(f"perimeter of the triangle is: {perimeter}")

#6 

# formula rectangle area: area = length * width 

def calculate_area_rectangle():
    length = int(input(">Length of the rectangle \n "))
    width = int(input(">Width of the rectangle \n "))
    return length * width

print(calculate_area_rectangle())



def area_of_circle():
    radius = int(input('>Radius of circle \n '))
    pi = 3.14
    return pi * radius * radius
    
print(area_of_circle())

# 8 - 11 I suck at math.

#12 - 14

case_1 = 'python'
case_2 = 'jargon'

print(len(case_1) != len(case_2))

on_is_in = 'on' in case_1 and 'on' in case_2

print(on_is_in)


phrase = "I hope this course is not full or jargon"

is_jargon_in = 'jargon' in phrase

print(is_jargon_in)

is_not_in = 'on' not in case_1 and 'on' not in case_2
print(is_not_in)

# #16

txt = 'python'
len_txt = len(txt)
float_txt = float(len_txt)
str_txt = str(float_txt)

#17

num = 6

if (num % 2) == 0:
    print('even number')
else:
    print('odd number')
 
 #18 - Not clear
    
floor_division = 3 // 2
print(floor_division)


#19 
ten_str = '10'
ten_int = 10
is_equal = ten_int == ten_str
print(is_equal)

#20 


# 21


def calc_person_pay():     
    hours = int(input(">How many hours a day do you work? \n"))
    rate= float(input(">What rate are you paid? \n"))

    person_pay = hours * rate

    print('Your pay ought to be: N', person_pay)
    
calc_person_pay()


#22

years_lived = int(input("How many years have you lived? \n"))

def calculate_seconds_lived(years):
    seconds_per_year  = 31536000
    seconds_lived = years * seconds_per_year
    print(f"Years lived: {years}")
    print("You have lived for roughly {:,}".format(seconds_lived) + " seconds")

calculate_seconds_lived(years_lived)

# 23

# use escape sequences in strings to solve this


