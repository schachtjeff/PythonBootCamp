numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

range_list = [x*2 for x in range(1, 5)]
print(range_list)

# Conditional comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

caps_names = [caps.upper() for caps in names if len(caps) > 4]
print(caps_names)

#Exercise with squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)