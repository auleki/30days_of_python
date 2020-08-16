# def generate_full_name (first_name, last_name):
#   full_name = f"Fullname is {first_name} {last_name}"
#   # print(full_name)
#   return full_name
  

# phrase = generate_full_name("Felix", "Canter")

# print(phrase)
# for



# def sum_of_numbers(n):
#   total = 0
#   for i in range(n + 2): 
#     total += i
#     print(i)

#   print(total)
# sum_of_numbers(5)
# sum_of_numbers(100)

# for i in range(5, 10):
#   print(i, end=', ')


# start = 2
# stop = 9 
# step = 1 
# stop += step

# for i in range(start, stop, step):
#   print(i, end=', ')


# def multi_params(*one):
#   phrase = f"{one} - {two} - {three} - {four}"
#   print(phrase)

# multi_params(one='first', two='second', three='third')


# def sum_all_nums(*nums):
#   total = 0 
#   for num in nums:
#     total += num
#     return total
# print(sum_all_nums(9, 10, 30))

def generate_groups(team, *args):
  print(f'Team: {team}')
  for i in args: 
    print(f'I: {i}')
generate_groups('Team-1', 'Aughost', 'Giwa', 'Germany')