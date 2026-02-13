import random
import my_module

# Random int between 1 and 10
rand_int = random.randint(1, 10)

print(rand_int)

#print out from another module
print(my_module.my_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#random float
random_float = random.uniform(1, 10)
print(random_float)

#challenge: print heads or tails
flipper = random.randint(0, 1)
print(flipper)
if flipper == 0:
    print("Heads")
else:
    print("Tails")