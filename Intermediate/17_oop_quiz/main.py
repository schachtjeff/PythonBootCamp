# Creating a class
class User:
    def __init__(self, user_id, username, followers = 0):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = followers

user_1 = User(user_id="001", username="Jeff")
# attributes attached to the object
#user_1.id = "001"
#user_1.username = "Jeff"

print(user_1.username)

user_2 = User(user_id="002", username="Steve")
#user_2.id = "002"
#user_2.username = "Steve"

print(user_2.username)
