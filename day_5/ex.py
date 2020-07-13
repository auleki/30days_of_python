nums = [4, 8, 1, 5, 9, 7, 3, 10, 2, 6 ]
alphabets = ["e", "g", "d", "c", "f", "b", "a"]
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
fruits = ['banana', 'orange', 'mango', 'lemon', 'Sweden']
web_techs = ['HTML', 'CSS', 'JS', 'React','React','Redux', 'Node', 'MongDB']
names = ["Kemi", "Sade", "Henry"]

series = [3, 4, 3, 4, 6, 114, 14, 5, 6, 3, 114]
digs = [45, 1, 84, 34, 24, 67, 89, 77, 334]

first, second, third, fourth, *rest, nine, tenth = nums
gr, fr, bg, sw, *others, ic, es = countries
list_1 = list()
list_2 = []
lang_1, lang_2, lang_3, *rest = web_techs
last_index = len(web_techs) - 1 
last_item = web_techs[-1]
country_amnt = len(countries)
all_countries = countries[0: 9]
reverse_countries = countries[-9:]
does_exist = "Belgium" in countries
name_and_tech = names + web_techs

all_life = fruits.extend(countries)
# print(web_techs.count("React"))
# print(series.index(4))
# digs.sort(reverse=True)

nums.sort()
alphabets.sort(reverse=True)

sorted_nums = sorted(nums, reverse = True)

print(nums)
print(alphabets)
print(sorted_nums)











# user_input = input("> Your name please \n ")
# names.insert(2, user_input)
# print(names)
# menu_items = ["items2", "items1"]
# menu_items.pop(0)
# # menu_items.remove("items2")
# # menu_items.remove(0)
# last_name = len(names) - 1
# del names
# print(names)
# names.clear()
# print(names)
# name_dup = names.copy() 
# print(name_dup)
# print(reverse_countries)
# print(country_amnt)
# print(gr, fr, bg)
# print(others)
# print(ic, es)
# print(first, second, third, fourth)
# print(rest)
# print(nine, tenth)
# print(rest)
# print(last_index)
# print(last_item)
# print(len(list_1), len(list_2))
# print(len(fruits), len(web_techs))
# print(lang_1, lang_2, lang_3, rest)

