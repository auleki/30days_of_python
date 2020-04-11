f_name = 'Wahab'
l_name = 'Giwa'
language = 'Javascript'


# OLD STYLE OF FORMATTING
''' formatted_string = 'I am %s %s. I teach %s' %(f_name, l_name, language)
print(formatted_string)

npm_packages = ['lodash', 'express', 'passport', 'bcrypt', 'nodemon']
formatted_string = 'Here are some NPM packages: ' % npm_packages '''


# NEW STYLE OF FORMATTING
formatted_string = 'I am {} {}. I teach {}'.format(f_name, l_name, language)
print(formatted_string)
a = 5750
b = 495

print('Multiplication: {} * {} = {}'.format(a, b, a * b))

# {:.2f} -- works as significant numbers
print('Divide: {} / {} = {:.2f}'.format(a, b, a / b))


radius = 567
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of radius {} is {:.2f}.'.format(radius, area)
print(formatted_string)


a = 4
b = 7
z = 19

print(f'{a} + {b} = {a + b}')
#observe the string format to show the result 
print(f'{z} / {b} = {z / b:.1f}')


''' a, b, c, d, e, f = language '''

''' 
print(a)
print(b)
print(c)
print(d)
print('-')
print(e)
print(f) 

'''

print(language)
# Finding last letter of dynamic string
''' 
last_index = len(language) - 1 
last_letter = language[last_index] 

'''

# OR 

# Finding the last 
''' last_letter = language[-1]

print(last_letter) '''

''' 
first_three = language[0:3]
print(first_three)
ranged_pick = language[3:6]
print(ranged_pick)
last_three = language[-3:]
print(last_three)
from_index_three = language[3:]
print(from_index_three)
 '''
# Reverse string
''' greet = "Hello, my people!"
print(greet[::-1]) '''

# skip characters while slicing with the , 
''' ran = language[0,3:5]
print(ran) '''


text = '  learning with asabeneh  '
text_2 = 'No wE arE loOkinG for GOLD'

''' capitalize = text.capitalize()
print(capitalize)  '''

# print(text.find('e'))
''' 
tech = ['React', ' Redux', ' Context', ' Ant']
hashed = "#".join(tech)
print(hashed)
 '''

# stripper = text.strip('g')
# print(text.strip('ng'))

# replaced = text.replace('with', 'with amazing').strip('')
# capital = text.title()
swapped = text_2.swapcase()
print(swapped)