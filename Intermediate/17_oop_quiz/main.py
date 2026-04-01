# Creating a class
class User:
    def __init__(self, user_id, username, followers = 0, following = 0):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(user_id="001", username="Jeff")
# attributes attached to the object
#user_1.id = "001"
#user_1.username = "Jeff"


print(user_1.username)

user_2 = User(user_id="002", username="Steve")
#user_2.id = "002"
#user_2.username = "Steve"
user_1.follow(user_2)

print(user_2.username)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
