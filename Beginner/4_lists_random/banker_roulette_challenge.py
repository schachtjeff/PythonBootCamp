import random

#Pick a random name from the list of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

rand_freind = random.randint(0, 4)
print(f"The winner is: {friends[rand_freind]}")

# Another option
print(random.choice(friends))