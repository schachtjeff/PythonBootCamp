
#prints 1 to 10
for number in range(1, 11):
    print(number)

#prints 1 to 10, with step of 3
for number in range(1, 11, 3):
    print(number)

# Gauss Challenge
total_nums = 0
for number in range(1, 101):
    total_nums += number
print(total_nums)