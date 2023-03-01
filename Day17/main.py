class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1

user_1 = User(1,"Fouzan")
user_2 = User(2,"NAMESAS")
user_1.follow(user_2)

print(user_2.followers)
print(user_1.followings)

