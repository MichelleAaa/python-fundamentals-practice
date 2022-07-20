class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# The first parameter of an instance method is self by default. Python handles passing in the argument for this parameter.
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)  # "janespassword"

# The method change_password() belongs to the user1 object, so to use it, you must use dot notation: objectname.methodname.
user1.change_password("bestpassword") #user1.password is now equal to "bestpassword"



