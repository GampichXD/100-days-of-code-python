class User:
    #Attributes
    def __init__(self, user_id, username): ##call every use class
        # print("It will be trigger")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #Methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","angela")
# user_1.id = "001"
# user_1.username = "angela"


print(user_1.id)
print(user_1.username)
print(user_1.followers)

user_2 = User("002","jack")
# user_2.id = "002"
# user_2.name = "jack"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#PascalCase
#camelCase
#snake_case