def square(x): 
  return x ** 2

def cube(x): 
  return x ** 3 

def absolute(x): 
  if x >= 0:
    return x
  else: 
    return -(x)

  
def high_order_function(type): 
  if type == 'square':
    return square
  elif type == 'cube': 
    return cube 
  elif type == 'absolute':
    return absolute

to_square = high_order_function('square')
# print(to_square(5))

to_cube = high_order_function('cube')
# print(to_cube(3))

to_absolute = high_order_function('absolute')
# print(to_absolute(-5))





def add_ten():
  ten = 10

  def add(num):
    return num + ten 
  return add 


closure_result = add_ten()

print(closure_result(19))

